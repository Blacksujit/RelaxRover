from datetime import datetime
from models.MistraL_model import get_mistral_response

# Mock databases or storage
mood_log = []
daily_check_in_log = set()  # Set to store dates when check-ins occurred

def log_mood(mood):
    """
    Logs the mood with a timestamp.
    """
    mood_log.append({'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'mood': mood})

def get_mood_log():
    """
    Retrieves the mood log.
    """
    return mood_log

def check_daily_in_check():
    """
    Checks if the user has already checked in today.
    """
    today = datetime.now().strftime('%Y-%m-%d')
    if today in daily_check_in_log:
        return True
    daily_check_in_log.add(today)
    return False

def handle_query(query):
    query = query.strip().lower()

    # Process specific queries related to mood logging and daily check-ins
    if query.startswith('log mood'):
        mood = query[len('log mood'):].strip()
        if mood:
            log_mood(mood)
            return {'mistral': f'Mood "{mood}" logged successfully.'}
        else:
            return {'mistral': 'Please provide a mood to log.'}
    
    elif query == 'get mood log':
        mood_entries = "\n".join([f"{entry['date']}: {entry['mood']}" for entry in get_mood_log()])
        return {'mistral': f"Mood Log:\n{mood_entries if mood_entries else 'No mood entries found.'}"}

    elif query == 'check in':
        if check_daily_in_check():
            return {'mistral': 'You have already checked in today.'}
        else:
            return {'mistral': 'You have successfully checked in today.'}
    
    # Process general queries using the Mistral model
    mistral_response = get_mistral_response(query)
    
    # Combine responses or choose one
    combined_response = {
        'mistral': mistral_response,
    }
    
    return combined_response
