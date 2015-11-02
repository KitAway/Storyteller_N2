'''
Created on Oct 16, 2015

@author: d038395
'''

##----------------------------   server parameters  --------------------------##
#SERVER_PORT             =   9999
#SERVER_PORTS            =   9998
#SERVER_HOST             =   'denethor.cdsdom.polito.it'
#NUMBER_OF_ENGINES       =   1

#LANGUAGE_SUPPORT        =   ['en-us','en-gb','it-it','zh-cn']
##-------------------------   task parameters  -------------------------------##
NUM_MULTI_TASKS         =   5
UPDATE_TIME_SECOND      =   1
QUERYING_TIME           =   3
DISPLAY_UPDATE_SECOND   =   3

NUM_OF_KEYWORDS         =   6
TITLE_FACTOR            =   2
RECOG_AUDIO_FORMAT      =   ['.wav','.mp3']

NUM_TAB_PRINT           =   1
NUM_SPACE_PRINT         =   12
##-----------------------------   task stutus   ------------------------------##
TASK_STATUS_INITIALED   =   'INITIALLED'
TASK_STATUS_LOCKED      =   'LOCKED'
TASK_STATUS_PROGRESS    =   'PROGRESSING'
TASK_STATUS_QUEUED      =   'QUEUED'
TASK_STATUS_FINISHED    =   'FINISHED'
TASK_STATUS_FAILED      =   'FAILED'
TASK_STATUS_SUBMIT      =   'SUBMITTED'
TASK_STATUS_NOT_FOUND   =   'TASK NOT FOUND'
##-----------------------------   task description   -------------------------##
TASK_DESCR_NONE         =   None
TASK_DESCR_SERVER       =   'Server gets Error.'
TASK_DESCR_FILE         =   'File is not recognized.'
TASK_DESCR_MISS         =   'Task is missed from the server.'
TASK_DESCR_CONNECTION   =   'Connection Failed to the server.'
TASK_DESCR_GOT          =   'Status from server.'
TASK_DESCR_ANALYSIS     =   'File analysis is failed.'
TASK_DESCR_STATUS       =   'Unknow status from server.'
TASK_DESCR_EXCEPTION    =   'Exception happend.'
TASK_DESCR_UNICODE      =   'Unicode Encode Error.'
##-----------------------------   stop words list  ---------------------------##

STOP_WORDS_LIST_ZH=['.',',','\u7684','\u4e00','\u4e0d','\u5728','\u4eba','\u6709','\u662f',
                    '\u4e3a','\u4ee5','\u4e8e','\u4e0a','\u4ed6','\u800c','\u540e',
                    '\u4e4b','\u6765','\u53ca','\u4e86','\u56e0','\u4e0b','\u53ef',
                    '\u5230','\u7531','\u8fd9','\u4e0e','\u4e5f','\u6b64','\u4f46',
                    '\u5e76','\u4e2a','\u5176','\u5df2','\u65e0','\u5c0f','\u6211',
                    '\u4eec','\u8d77','\u6700','\u518d','\u4eca','\u53bb','\u597d',
                    '\u53ea','\u53c8','\u6216','\u5f88','\u4ea6','\u67d0','\u628a',
                    '\u90a3','\u4f60','\u4e43','\u5b83','\u5427','\u88ab','\u6bd4',
                    '\u522b','\u8d81','\u5f53','\u4ece','\u5230','\u5f97','\u6253',
                    '\u51e1','\u513f','\u5c14','\u8be5','\u5404','\u7ed9','\u8ddf',
                    '\u548c','\u4f55','\u8fd8','\u5373','\u51e0','\u65e2','\u770b',
                    '\u636e','\u8ddd','\u9760','\u5566','\u4e86','\u53e6','\u4e48',
                    '\u6bcf','\u4eec','\u561b','\u62ff','\u54ea','\u90a3','\u60a8',
                    '\u51ed','\u4e14','\u5374','\u8ba9','\u4ecd','\u5565','\u5982',
                    '\u82e5','\u4f7f','\u8c01','\u867d','\u968f','\u540c','\u6240',
                    '\u5979','\u54c7','\u55e1','\u5f80','\u54ea','\u4e9b','\u5411',
                    '\u6cbf','\u54df','\u7528','\u4e8e','\u54b1','\u5219','\u600e',
                    '\u66fe','\u81f3','\u81f4','\u7740','\u8bf8','\u55ef']


STOP_WORDS_LIST_IT=[',','.', 'a','adesso', 'ai', 'al', 'alla', 'allo', 'allora', 'altre', 'fa',
            'altri', 'altro', 'anche', 'ancora', 'avere', 'aveva', 'avevano', 'bene','dove',
            'ben', 'buono', 'che', 'chi', 'cinque', 'comprare', 'con', 'come', 'i','tutto','prima',
            'consecutivi', 'consecutivo', 'cosa', 'cui', 'da', 'dal','dai', 'dalla', 'proprio',
            'dalle','del', 'dei', 'in','si','ci','se','mi','pi\u00f9','cos\u00ec', 'essere','perdono',
            'della', 'dello', 'dentro', 'deve', 'devo', 'di', 'doppio', 'perch\u00e9', 'magari',
            'due', 'e','\u00e8', 'ecco', 'fare', 'fine', 'fino', 'fra', 'gente', 'quando', 'gi\u00e0',
            'giu', 'ha', 'hai', 'hanno', 'ho', 'il', 'indietro', 'invece', 'ti', 'tu', 'era', 'mio',
            'io', 'la', 'lavoro', 'le', 'lei', "l'",'lo', 'loro', 'lui', 'lungo','per\u00f2', 'so',
            'ma', 'me', 'meglio', 'molta', 'molti', 'molto', 'nei', 'nella', 'questi', 'mia',"dell'",
            'no', 'noi','non' ,'nome', 'nostro', 'nove', 'nuovi', 'nuovo', 'o', 'cose', 'qualcosa',
            'oltre', 'ora', 'otto', 'peggio','per', 'pero', 'persone', 'piu', 'persona','vedere',
            'poco', 'primo', 'promesso', 'qua', 'quarto', 'quasi', 'quattro', 'questa','sua', 'parte',
            'quella', 'quel', 'quello', 'questo', 'qui', 'quindi', 'quinto', 'rispetto', 'sara', 'tutti',
            'queste','secondo', 'sei', 'sembra', 'sembrava', 'senza', 'sette', 'sia', 'sempre', 'pu\u00f2',
            'siamo', 'siete', 'solo', 'sono', 'sopra', 'soprattutto', 'sotto','abbiamo', 'dire','faccio',
            'stati', 'stato', 'stesso', 'su', 'subito', 'sul', 'sulla', "c'\u00e8",'forse','dopo',
            'tanto', 'te', 'tempo', 'terzo', 'tra', 'tre', 'triplo', 'ultimo', 'gli','poi', 'penso',
            "un'",'un', 'una', 'uno', 'va', 'vai', 'voi', 'volte', 'vostro','suo','fatto','detto']

STOP_WORDS_LIST_EN=[',','.','a', 'about', 'above', 'after', 'again', 'against', 'all',
             'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been',
             'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot',
             'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing',
             "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had',
             "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll",
             "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his',
             'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is',
             "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most',
             "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once',
             'only', 'or', 'other', 'ought', 'our',  'ours', 'ourselves', 'out', 'over',
             'own', 'same', "shan't", 'she', "she'd", "she'll", "she's",  'should',
             "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their',
             'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to',
             'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll",
             "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where',
             "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with',
             "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves', "a's", 'able', 'about', 'above',
             'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again',
             'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along',
             'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and',
             'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
             'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't",
             'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available',
             'away', 'awfully', 'be', 'became', 'because', 'become', 'becomes', 'becoming',
             'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside',
             'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by',
             "c'mon", "c's", 'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes',
             'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes',
             'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing',
             'contains', 'corresponding', 'could', "couldn't", 'course', 'currently',
             'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does',
             "doesn't", 'doing', "don't", 'done', 'down', 'downwards', 'during', 'each','edu',
             'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially',
             'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything',
             'everywhere', 'ex', 'exactly', 'example', 'except', 'far', 'few', 'fifth',
             'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly',
             'forth', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting',
             'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings',
             'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't",
             'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here', "here's",
             'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him',
             'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', "i'd",
             "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch',
             'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar',
             'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's",
             'its', 'itself', 'just', 'keep', 'keeps', 'kept', 'know', 'known','knows',
             'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let',
             "let's", 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd',
             'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might',
              'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'name',
            'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither',
            'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none',
            'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously',
             'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones',
             'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours',
            'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular','particularly',
            'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably',
            'provides', 'que', 'quite', 'qv', 'rather', 'rd','re', 'really', 'reasonably',
            'regarding', 'regardless', 'regards', 'relatively','respectively', 'right', 'said',
            'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem',
            'seemed', 'seeming', 'seems', 'seen', 'self',  'selves', 'sensible', 'sent', 'serious',
            'seriously', 'seven', 'several', 'shall',  'she', 'should', "shouldn't", 'since',
            'six', 'so', 'some', 'somebody', 'somehow',   'someone', 'something', 'sometime',
            'sometimes', 'somewhat', 'somewhere', 'soon','sorry', 'specified', 'specify',
            'specifying', 'still', 'sub', 'such', 'sup',     'sure', "t's", 'take', 'taken',
             'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's",
             'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence',
             'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres',
             'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think',
             'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through',
             'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards',
             'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'un', 'under',
              'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use',
              'used', 'useful', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via',
              'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll",
              "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's",
             'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter',
             'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which',
             'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why',
             'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'would',
             "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your',
             'yours', 'yourself', 'yourselves', 'zero']

def main():
    s='\u7684'
    if s in STOP_WORDS_LIST_ZH:
        print(s+' is in the list')
    else:
        print(s+' is not in list')
if __name__=='__main__':
    main()
