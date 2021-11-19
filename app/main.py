"""
TDD app entry point
"""

APP_NAME = 'TDD'


def greeting_message() -> str:
    """Get the default greeting message

    :return: The formatted greeting message
    """
    return f'Welcome to {APP_NAME} !'


if __name__ == '__main__':
    print(greeting_message())
