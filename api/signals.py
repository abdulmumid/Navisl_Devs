from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactRequest, Consult, JobApplication

import telebot
import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from django.utils.timezone import localtime


# Настройка логгера
logger = logging.getLogger(__name__)

# Загрузка переменных окружения из .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

# Получение токена бота и chat_id из переменных окружения
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

if not token:
    logger.error("TELEGRAM_BOT_TOKEN не найден в .env!")
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env!")

# Инициализация Telegram бота
bot = telebot.TeleBot(token)


def send_message_with_file(message, file_field):
    """
    Отправляет сообщение в Telegram чат и прикрепляет файл, если он есть и доступен.
    """
    try:
        bot.send_message(chat_id, message)

        # Проверяем, что файл существует и доступен
        if file_field and hasattr(file_field, 'path') and os.path.exists(file_field.path):
            with open(file_field.path, 'rb') as f:
                bot.send_document(chat_id, f)
        elif file_field:
            logger.warning(f"Файл не найден или недоступен: {getattr(file_field, 'path', 'нет пути')}")
    except Exception as e:
        logger.error(f"[Signal] Ошибка отправки Telegram сообщения: {e}")


# --- Сигналы Django для отправки уведомлений в Telegram ---

@receiver(post_save, sender=ContactRequest)
def notify_contact_request(sender, instance, created, **kwargs):
    """
    Отправляет уведомление при создании новой заявки ContactRequest
    """
    if created:
        message = (
            f'📩 Новая заявка: {instance.phone}\n'
            f'Email: {instance.email}\n\n'
            f'Дата: {localtime(instance.created_at).strftime("%Y-%m-%d %H:%M:%S")}'
        )
        send_message_with_file(message, getattr(instance, 'file', None))


@receiver(post_save, sender=Consult)
def notify_consult_request(sender, instance, created, **kwargs):
    """
    Отправляет уведомление при создании новой заявки Consult
    """
    if created:
        message = (
            f"🗨 Новая заявка на консультацию:\n"
            f"Имя: {instance.name}\n"
            f"Телефон: {instance.phone}\n"
            f"Текст: {instance.text}"
        )
        send_message_with_file(message, None)  # В Consult нет файла? Передаем None


@receiver(post_save, sender=JobApplication)
def notify_job_application(sender, instance, created, **kwargs):
    """
    Отправляет уведомление при создании нового отклика на вакансию
    """
    if created:
        message = (
            f'💼 [Новый отклик] {instance.name} откликнулся на вакансию "{instance.job.title}"\n'
            f'Телефон: {instance.phone}\n'
            f'Email: {instance.email}\n'
            f'LinkedIn: {instance.linkedin_url}\n'
            f'Дата: {localtime(instance.applied_at).strftime("%Y-%m-%d %H:%M:%S")}'
        )
        send_message_with_file(message, getattr(instance, 'file', None))
