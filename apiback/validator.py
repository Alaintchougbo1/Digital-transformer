from django.core.exceptions import ValidationError

def validate_image_file(file):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    import os
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError(f"Unsupported file format. Supported formats are: {', '.join(valid_extensions)}")
