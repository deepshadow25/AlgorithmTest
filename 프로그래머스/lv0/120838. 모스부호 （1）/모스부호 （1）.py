morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
def solution(letter):
    answer = ''
    keys = list(morse.keys())
    values = list(morse.values())
    letter = letter.split(' ')
    for i in range(len(letter)):
        for j in range(len(keys)):
            if letter[i] == keys[j]:
                answer += values[j]
    return answer