#!/bin/bash

echo "apply celery worker"
celery -A sms_gateway worker -l info
