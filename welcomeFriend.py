# This attempts to be (more or less) the simplest possible hello world Alexa skill...

from __future__ import print_function
import random

global joke_count
global secret_count
global song_count
global food_count
global quote_count
global game_count
joke_count = 0
secret_count = 0
song_count = 0
food_count = 0
quote_count = 0
game_count = 0
# We'll start with a couple of globals...
CardTitlePrefix = "Greeting"

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """
    Build a speechlet JSON representation of the title, output text, 
    reprompt text & end of session
    """

    return {
        'outputSpeech': {
           'type': 'SSML',
            'ssml': "<speak>"+output+"</speak>"
       },

        'card': {
            'type': 'Simple',
            'title': CardTitlePrefix + " - " + title,
            'content': output
        },
        
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>"+reprompt_text+"</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    """
    Build the full response JSON from the speechlet response
    """
    print("**** Session Attributes: " +str(session_attributes))
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():    
    card_title = "Hello"
    speech_output = "Hi Mayank. I welcome your friend? Introduce me."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I'm sorry - I didn't get your friend name. It's either complicated or your pronunciation is bad."
    should_end_session = False
    session_attributes = {  "speech_output": speech_output,
                            "reprompt_text": reprompt_text
                  }
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request(session):
    card_title = "Session Ended"
    friend_name = session['attributes']['friend_name']
    speech_output = "It was nice meeting you " + friend_name + ". But before going let me tell you this, DATE HIM."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    joke_count = 0
    secret_count = 0
    song_count = 0
    food_count = 0
    quote_count = 0
    game_count = 0
    return build_response({}, build_speechlet_response(
        card_title, speech_output, "Good Bye", should_end_session))

def say_hello_to_girl(friend_name):
    """
    Return a suitable greeting...
    """
    card_title = "Greeting Message"
    greeting_string =   "Hi "+friend_name+"! Welcome to Mayank's adobe. He has told me about you. "\
                        "You seem to be more beautiful then he has mentioned. "\
                        "Do you want to listen anything specific about him. "\
                        "Say Joke or Secret or Songs. You can also say food or quote or game."

    should_end_session = False
    session_attributes = {  
                            "speech_output": greeting_string,
                            "friend_name" : friend_name
                         }

    return build_response(session_attributes, build_speechlet_response(card_title, greeting_string, "Ask me to say hello...", should_end_session))

def say_hello_to_boy(friend_name):
    """
    Return a suitable greeting...
    """
    card_title = "Greeting Message"
    greeting_string = "Hi "+friend_name+"! Welcome to Mayank's adobe. This is unusual to have a guy in mikki's room. Anyway, I welcome you here."# Have you brought him anything to eat?"
    should_end_session = True
    session_attributes = {  
                            "speech_output": greeting_string,
                            "friend_name" : friend_name
                            
                         }

    return build_response(session_attributes, build_speechlet_response(card_title, greeting_string, "Ask me to say hello...", should_end_session))

def fall_back_message():
    """
    Return a suitable greeting...
    """
    card_title = "Fallback Message"
    fallback_string = "Sorry. I couldn't understood it. Please say again."
    should_end_session = False
    session_attributes = {  
                            "speech_output": fallback_string,
                            
                            
                         }

    return build_response(session_attributes, build_speechlet_response(card_title, fallback_string, "Ask me to say hello...", should_end_session))


def joke_story(session):

    global joke_count
    friend_name = session['attributes']['friend_name']
    secret_count = 0
    song_count = 0
    food_count = 0
    quote_count = 0
    game_count = 0

    joke_story = [
                    "Mayank dances like chimpanzee. Please don't laugh on him " + friend_name,
                    "Once he was fallen in love with his maths teacher.",
                    "His parents still teases him about his first girl as friend.",
                    "He is very shy guy. Don't take it seriously "+ friend_name+ ". You know it's a joke.",
                    "He fumbles with words in front of beautiful girls. I am pretty sure it would have happened in front of you too " + friend_name
                ]
    card_title = "Joke Story"

    if joke_count >= len(joke_story) :
        joke_string = "I don't have more stories right now. But I will make sure to gather more. Good Bye. Nice meeting you " + friend_name
        should_end_session = True
    else :    
        joke_string = joke_story[joke_count] + ". Do you want to hear another one? Just say joke"
        should_end_session = False
        joke_count += 1  
    
    session_attributes = {
        "friend_name"  : friend_name,
        "Joke_Count"   : joke_count,
        "Secret_Count" : secret_count,
        "Song_Count"   : song_count,
        "Food_Count"   : food_count,
        "Quote_Count"  : quote_count,
        "Game_Count"   : game_count
    }
    return build_response(session_attributes, build_speechlet_response(card_title, joke_string, "Please repeat it again..", should_end_session))

def favorite_food(session):

    global food_count
    friend_name = session['attributes']['friend_name']

    joke_count = 0
    secret_count = 0
    song_count = 0
    quote_count = 0
    game_count = 0

    food_story = [
                    "Rice and Rajma. You know what. You can feed him sometime " + friend_name +". He is always hungry",
                    "Pizza. He craves for pizza. Just say the word and he will order for you too " + friend_name,
                    "Pasta. He is crazy for pasta. You should ask him to treat you sometime.",
                    "Salad. Sometimes he care for his weight for a change. I think you would love to go and have salad with him " + friend_name
                ]
    card_title = "Favorite Food"

    print("****food count: "+ str(food_count))
    if food_count >= len(food_story) :
        food_string = "He like these many only. If he likes anything else, i will surely tell you. Good Bye. Nice meeting you " + friend_name
        should_end_session = True
    else :    
        food_string = "His favorite food is " + food_story[food_count] + ". Do you want to hear another one? Just say food"
        food_count += 1
        should_end_session = False    
    
    session_attributes = {
        
        "friend_name"  : friend_name,
        "Joke_Count"   : joke_count,
        "Secret_Count" : secret_count,
        "Song_Count"   : song_count,
        "Food_Count"   : food_count,
        "Quote_Count"  : quote_count,
        "Game_Count"   : game_count
    }
    return build_response(session_attributes, build_speechlet_response(card_title, food_string, "Please repeat it again..", should_end_session))

def secret_story(session):

    global secret_count
    friend_name = session['attributes']['friend_name']

    secret_story = [
                    "He is still crazy for toy cars. Don't you too find it funny " + friend_name,
                    "Don't ever ask him school, college marks. He won't ever tell you.",
                    friend_name + " his room might be clean but check his closed too. There you will be surprised.",
                    "He is scared of high speed driving because of his accident but am sure to impress you he will definitely drive fast. Go for bike rides with him " + friend_name
                ]
    card_title = "Mayank's Secret"

    print("****secret count: "+ str(secret_count))
    if secret_count >= len(secret_story) :
        secret_string = "Till now i could find only there. If i find anything else, i will surely tell you. Good Bye. Nice meeting you " + friend_name
        should_end_session = True
    else :    
        secret_string = "One of his secret is that " + secret_story[secret_count] + ". Do you want to hear another one? Just say secret"
        secret_count += 1
        should_end_session = False    
    
    session_attributes = {
        
        "friend_name"  : friend_name,
        "Joke_Count"   : joke_count,
        "Secret_Count" : secret_count,
        "Song_Count"   : song_count,
        "Food_Count"   : food_count,
        "Quote_Count"  : quote_count,
        "Game_Count"   : game_count
    }
    return build_response(session_attributes, build_speechlet_response(card_title, secret_string, "Please repeat it again..", should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they want """

    #print("****on_launch requestId=" + launch_request['requestId'] +
     #     ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    
    print (intent)
    try :
        intent_name_value = intent['slots']['friend_name']['value']
    except :
        print("**** Can't find name")

    try:  
        intent_gender_value = intent['slots']['gender']['value']
        # print("****intent_gender_value: " + intent_name_value)
    except :
        print("**** Can't find gender")

    #friend_name = intent_value
    print("****session: " + str(session))
    print("****Intent found is: " + str(intent))
    print("****Intent Name found is: " + str(intent_name))
    #print("****intent_gender_value found is: " + str(intent_gender_value))
    # Dispatch to your skill's intent handlers
    if intent_name == "welcomeIntent" and (intent_gender_value == "her" or intent_gender_value == "she"):
        return say_hello_to_girl(intent_name_value)
    elif intent_name == "welcomeIntent" and (intent_gender_value == "his" or intent_gender_value == "he"):
        return say_hello_to_boy(intent_name_value)        
    elif intent_name == "jokeIntent" :
        return joke_story(session)
    elif intent_name == "foodIntent" :
        return favorite_food(session)
    elif intent_name == "secretIntent" :
        return secret_story(session)
    elif intent_name == "songIntent" :
        return favorite_song(session)
    elif intent_name == "quoteIntent" :
        return favorite_quote(session)
    elif intent_name == "gameIntent" :
        return favorite_game(session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request(session)
    elif intent_name == "AMAZON.FallbackIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session. Is not called when the skill returns should_end_session=true """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])


    if event['session']['new']:
        print ("**** Reached")
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    print("**** Intent coming is : " + event['request']['type'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])