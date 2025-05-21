from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactRequest, Consult, JobApplication

import telebot
import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from django.utils.timezone import localtime


# Инициализация общих параметров
logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

token = os.getenv('TELEGRAM_BOT_TOKEN')  # теперь можно использовать .env
chat_id = os.getenv('TELEGRAM_CHAT_ID', '-1002120990081')  # по умолчанию ваш ID

if not token:
    logger.error("TELEGRAM_BOT_TOKEN не найден в .env!")
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env!")

bot = telebot.TeleBot(token)


def send_message_with_file(message, file_field):
    try:
        bot.send_message(chat_id, message)
        if file_field and file_field.path and os.path.exists(file_field.path):
            with open(file_field.path, 'rb') as f:
                bot.send_document(chat_id, f)
        elif file_field:
            logger.warning(f"Файл не найден: {file_field.path}")
    except Exception as e:
        logger.error(f"[Signal] Ошибка отправки Telegram: {e}")


# --- Сигналы ---

@receiver(post_save, sender=ContactRequest)
def notify_contact_request(sender, instance, created, **kwargs):
    if created:
        message = (
            f'📩 Новая заявка: {instance.phone}\n'
            f'Email: {instance.email}\n\n'
            f'Дата: {localtime(instance.created_at).strftime("%Y-%m-%d %H:%M:%S")}'
        )
        send_message_with_file(message, instance.file)


@receiver(post_save, sender=Consult)
def notify_consult_request(sender, instance, created, **kwargs):
    if created:
        message = f"Новая заявка на консультацию:\nИмя: {instance.name}\nТелефон: {instance.phone}\nТекст: {instance.text}"
        send_message_with_file(message, instance)


@receiver(post_save, sender=JobApplication)
def notify_job_application(sender, instance, created, **kwargs):
    if created:
        message = (
            f'[Новый отклик] {instance.name} откликнулся на вакансию "{instance.job.title}"\n'
            f'Телефон: {instance.phone}\n'
            f'Email: {instance.email}\n'
            f'LinkedIn: {instance.linkedin_url}\n'
            f'Дата: {localtime(instance.applied_at).strftime("%Y-%m-%d %H:%M:%S")}'
        )
        send_message_with_file(message, instance.file)
