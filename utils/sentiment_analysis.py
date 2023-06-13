from snownlp import SnowNLP


def get_emotional_score(text):
    score = 0.0
    http_code = 500
    try:
        score = SnowNLP(text).sentiments
        http_code = 200
    except Exception as error:
        print("error", error)
    return http_code, score
