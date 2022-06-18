def solution(message, K):
    # write your code in Python 3.6
    message = str(message)
    if K >= len(message):
        return message

    cropped_msg = message[:K]
    if cropped_msg[-1] == " ":
        return cropped_msg[:-1]
    elif message[len(cropped_msg)] != " ":
        last_space = len(cropped_msg) - 1 - cropped_msg[::-1].index(" ")
        cropped_msg = cropped_msg[:last_space]
        return message[:last_space]

print(solution("A quick brown fox jumps over the lazy dog", 39))