# $ANTLR 3.4.1-SNAPSHOT Imp.g 2013-07-03 15:48:45

import sys
from Imp.antlr3 import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__50=50
T__51=51
T__52=52
T__53=53
T__54=54
T__55=55
T__56=56
T__57=57
T__58=58
T__59=59
T__60=60
T__61=61
T__62=62
T__63=63
T__64=64
T__65=65
T__66=66
T__67=67
T__68=68
T__69=69
T__70=70
T__71=71
T__72=72
T__73=73
T__74=74
T__75=75
T__76=76
T__77=77
T__78=78
T__79=79
T__80=80
T__81=81
T__82=82
T__83=83
T__84=84
T__85=85
T__86=86
T__87=87
T__88=88
T__89=89
T__90=90
T__91=91
ANON=4
ASSIGN=5
ATTR=6
CALL=7
CLASS_ID=8
CLASS_REF=9
COMMENT=10
CONSTRUCT=11
DEF_DEFAULT=12
DEF_ENTITY=13
DEF_IMPLEMENT=14
DEF_IMPLEMENTATION=15
DEF_RELATION=16
DEF_TYPE=17
ENUM=18
ENUM_KEY=19
ESC_SEQ=20
EXPONENT=21
EXPRESSION=22
FALSE=23
FLOAT=24
FOR=25
HASH=26
HEX_DIGIT=27
ID=28
INCLUDE=29
INDEX=30
INT=31
LAMBDA=32
LIST=33
METHOD=34
ML_STRING=35
MULT=36
NONE=37
NS=38
OCTAL_ESC=39
OP=40
ORPHAN=41
REF=42
REGEX=43
STATEMENT=44
STRING=45
TRUE=46
UNICODE_ESC=47
VAR_REF=48
WS=49

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 50: "T__50", 51: "T__51", 52: "T__52", 53: "T__53", 54: "T__54", 
    55: "T__55", 56: "T__56", 57: "T__57", 58: "T__58", 59: "T__59", 60: "T__60", 
    61: "T__61", 62: "T__62", 63: "T__63", 64: "T__64", 65: "T__65", 66: "T__66", 
    67: "T__67", 68: "T__68", 69: "T__69", 70: "T__70", 71: "T__71", 72: "T__72", 
    73: "T__73", 74: "T__74", 75: "T__75", 76: "T__76", 77: "T__77", 78: "T__78", 
    79: "T__79", 80: "T__80", 81: "T__81", 82: "T__82", 83: "T__83", 84: "T__84", 
    85: "T__85", 86: "T__86", 87: "T__87", 88: "T__88", 89: "T__89", 90: "T__90", 
    91: "T__91", 4: "ANON", 5: "ASSIGN", 6: "ATTR", 7: "CALL", 8: "CLASS_ID", 
    9: "CLASS_REF", 10: "COMMENT", 11: "CONSTRUCT", 12: "DEF_DEFAULT", 13: "DEF_ENTITY", 
    14: "DEF_IMPLEMENT", 15: "DEF_IMPLEMENTATION", 16: "DEF_RELATION", 17: "DEF_TYPE", 
    18: "ENUM", 19: "ENUM_KEY", 20: "ESC_SEQ", 21: "EXPONENT", 22: "EXPRESSION", 
    23: "FALSE", 24: "FLOAT", 25: "FOR", 26: "HASH", 27: "HEX_DIGIT", 28: "ID", 
    29: "INCLUDE", 30: "INDEX", 31: "INT", 32: "LAMBDA", 33: "LIST", 34: "METHOD", 
    35: "ML_STRING", 36: "MULT", 37: "NONE", 38: "NS", 39: "OCTAL_ESC", 
    40: "OP", 41: "ORPHAN", 42: "REF", 43: "REGEX", 44: "STATEMENT", 45: "STRING", 
    46: "TRUE", 47: "UNICODE_ESC", 48: "VAR_REF", 49: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

class ImpLexer(Lexer):

    grammarFileName = "Imp.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa24 = self.DFA24(
            self, 24,
            eot = self.DFA24_eot,
            eof = self.DFA24_eof,
            min = self.DFA24_min,
            max = self.DFA24_max,
            accept = self.DFA24_accept,
            special = self.DFA24_special,
            transition = self.DFA24_transition
            )






    # $ANTLR start "T__50"
    def mT__50(self, ):
        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # Imp.g:7:7: ( '!=' )
            # Imp.g:7:9: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):
        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # Imp.g:8:7: ( '(' )
            # Imp.g:8:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):
        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # Imp.g:9:7: ( ')' )
            # Imp.g:9:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):
        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # Imp.g:10:7: ( ',' )
            # Imp.g:10:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):
        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # Imp.g:11:7: ( '--' )
            # Imp.g:11:9: '--'
            pass 
            self.match("--")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):
        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # Imp.g:12:7: ( '->' )
            # Imp.g:12:9: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):
        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # Imp.g:13:7: ( '.' )
            # Imp.g:13:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):
        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # Imp.g:14:7: ( ':' )
            # Imp.g:14:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):
        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # Imp.g:15:7: ( '::' )
            # Imp.g:15:9: '::'
            pass 
            self.match("::")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):
        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # Imp.g:16:7: ( '<' )
            # Imp.g:16:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__59"



    # $ANTLR start "T__60"
    def mT__60(self, ):
        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # Imp.g:17:7: ( '<-' )
            # Imp.g:17:9: '<-'
            pass 
            self.match("<-")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__60"



    # $ANTLR start "T__61"
    def mT__61(self, ):
        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # Imp.g:18:7: ( '<=' )
            # Imp.g:18:9: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__61"



    # $ANTLR start "T__62"
    def mT__62(self, ):
        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # Imp.g:19:7: ( '=' )
            # Imp.g:19:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__62"



    # $ANTLR start "T__63"
    def mT__63(self, ):
        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # Imp.g:20:7: ( '==' )
            # Imp.g:20:9: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__63"



    # $ANTLR start "T__64"
    def mT__64(self, ):
        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # Imp.g:21:7: ( '>' )
            # Imp.g:21:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):
        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # Imp.g:22:7: ( '>=' )
            # Imp.g:22:9: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):
        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # Imp.g:23:7: ( '[' )
            # Imp.g:23:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):
        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # Imp.g:24:7: ( ']' )
            # Imp.g:24:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):
        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # Imp.g:25:7: ( 'and' )
            # Imp.g:25:9: 'and'
            pass 
            self.match("and")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):
        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # Imp.g:26:7: ( 'as' )
            # Imp.g:26:9: 'as'
            pass 
            self.match("as")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):
        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # Imp.g:27:7: ( 'end' )
            # Imp.g:27:9: 'end'
            pass 
            self.match("end")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):
        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # Imp.g:28:7: ( 'entity' )
            # Imp.g:28:9: 'entity'
            pass 
            self.match("entity")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):
        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # Imp.g:29:7: ( 'extends' )
            # Imp.g:29:9: 'extends'
            pass 
            self.match("extends")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):
        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # Imp.g:30:7: ( 'for' )
            # Imp.g:30:9: 'for'
            pass 
            self.match("for")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):
        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # Imp.g:31:7: ( 'implement' )
            # Imp.g:31:9: 'implement'
            pass 
            self.match("implement")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):
        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # Imp.g:32:7: ( 'implementation' )
            # Imp.g:32:9: 'implementation'
            pass 
            self.match("implementation")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):
        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # Imp.g:33:7: ( 'in' )
            # Imp.g:33:9: 'in'
            pass 
            self.match("in")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):
        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # Imp.g:34:7: ( 'include' )
            # Imp.g:34:9: 'include'
            pass 
            self.match("include")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):
        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # Imp.g:35:7: ( 'index' )
            # Imp.g:35:9: 'index'
            pass 
            self.match("index")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):
        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # Imp.g:36:7: ( 'is' )
            # Imp.g:36:9: 'is'
            pass 
            self.match("is")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):
        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # Imp.g:37:7: ( 'matching' )
            # Imp.g:37:9: 'matching'
            pass 
            self.match("matching")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):
        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # Imp.g:38:7: ( 'not' )
            # Imp.g:38:9: 'not'
            pass 
            self.match("not")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):
        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # Imp.g:39:7: ( 'or' )
            # Imp.g:39:9: 'or'
            pass 
            self.match("or")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):
        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # Imp.g:40:7: ( 'parent' )
            # Imp.g:40:9: 'parent'
            pass 
            self.match("parent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):
        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # Imp.g:41:7: ( 'root' )
            # Imp.g:41:9: 'root'
            pass 
            self.match("root")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):
        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # Imp.g:42:7: ( 'typedef' )
            # Imp.g:42:9: 'typedef'
            pass 
            self.match("typedef")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):
        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # Imp.g:43:7: ( 'using' )
            # Imp.g:43:9: 'using'
            pass 
            self.match("using")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):
        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # Imp.g:44:7: ( 'when' )
            # Imp.g:44:9: 'when'
            pass 
            self.match("when")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):
        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # Imp.g:45:7: ( 'with' )
            # Imp.g:45:9: 'with'
            pass 
            self.match("with")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):
        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # Imp.g:46:7: ( '{' )
            # Imp.g:46:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):
        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # Imp.g:47:7: ( '|' )
            # Imp.g:47:9: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):
        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # Imp.g:48:7: ( '}' )
            # Imp.g:48:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__91"



    # $ANTLR start "ENUM_KEY"
    def mENUM_KEY(self, ):
        try:
            _type = ENUM_KEY
            _channel = DEFAULT_CHANNEL

            # Imp.g:272:2: ( 'enum' )
            # Imp.g:272:4: 'enum'
            pass 
            self.match("enum")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ENUM_KEY"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):
        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # Imp.g:276:2: ( 'true' )
            # Imp.g:276:4: 'true'
            pass 
            self.match("true")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):
        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # Imp.g:280:2: ( 'false' )
            # Imp.g:280:4: 'false'
            pass 
            self.match("false")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Imp.g:283:4: ( ( 'a' .. 'z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )* )
            # Imp.g:283:6: ( 'a' .. 'z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            pass 
            if self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Imp.g:283:22: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 45 or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Imp.g:
                    pass 
                    if self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "CLASS_ID"
    def mCLASS_ID(self, ):
        try:
            _type = CLASS_ID
            _channel = DEFAULT_CHANNEL

            # Imp.g:287:2: ( ( 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )* )
            # Imp.g:287:5: ( 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            pass 
            if (65 <= self.input.LA(1) <= 90):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Imp.g:287:16: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '-' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 45 or (48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Imp.g:
                    pass 
                    if self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CLASS_ID"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # Imp.g:290:5: ( ( '0' .. '9' )+ )
            # Imp.g:290:7: ( '0' .. '9' )+
            pass 
            # Imp.g:290:7: ( '0' .. '9' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # Imp.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # Imp.g:294:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt10 = 3
            alt10 = self.dfa10.predict(self.input)
            if alt10 == 1:
                # Imp.g:294:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                pass 
                # Imp.g:294:9: ( '0' .. '9' )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # Imp.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                self.match(46)

                # Imp.g:294:25: ( '0' .. '9' )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57)) :
                        alt5 = 1


                    if alt5 == 1:
                        # Imp.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop5


                # Imp.g:294:37: ( EXPONENT )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 69 or LA6_0 == 101) :
                    alt6 = 1
                if alt6 == 1:
                    # Imp.g:294:37: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt10 == 2:
                # Imp.g:295:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
                pass 
                self.match(46)

                # Imp.g:295:13: ( '0' .. '9' )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((48 <= LA7_0 <= 57)) :
                        alt7 = 1


                    if alt7 == 1:
                        # Imp.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


                # Imp.g:295:25: ( EXPONENT )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 69 or LA8_0 == 101) :
                    alt8 = 1
                if alt8 == 1:
                    # Imp.g:295:25: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt10 == 3:
                # Imp.g:296:9: ( '0' .. '9' )+ EXPONENT
                pass 
                # Imp.g:296:9: ( '0' .. '9' )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # Imp.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                self.mEXPONENT()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # Imp.g:300:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt16 = 3
            LA16_0 = self.input.LA(1)

            if (LA16_0 == 47) :
                LA16_1 = self.input.LA(2)

                if (LA16_1 == 47) :
                    alt16 = 1
                elif (LA16_1 == 42) :
                    alt16 = 3
                else:
                    nvae = NoViableAltException("", 16, 1, self.input)

                    raise nvae


            elif (LA16_0 == 35) :
                alt16 = 2
            else:
                nvae = NoViableAltException("", 16, 0, self.input)

                raise nvae


            if alt16 == 1:
                # Imp.g:300:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")


                # Imp.g:300:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                        alt11 = 1


                    if alt11 == 1:
                        # Imp.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop11


                # Imp.g:300:28: ( '\\r' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 13) :
                    alt12 = 1
                if alt12 == 1:
                    # Imp.g:300:28: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt16 == 2:
                # Imp.g:301:7: '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match(35)

                # Imp.g:301:11: (~ ( '\\n' | '\\r' ) )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((0 <= LA13_0 <= 9) or (11 <= LA13_0 <= 12) or (14 <= LA13_0 <= 65535)) :
                        alt13 = 1


                    if alt13 == 1:
                        # Imp.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop13


                # Imp.g:301:25: ( '\\r' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 13) :
                    alt14 = 1
                if alt14 == 1:
                    # Imp.g:301:25: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt16 == 3:
                # Imp.g:302:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # Imp.g:302:14: ( options {greedy=false; } : . )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 42) :
                        LA15_1 = self.input.LA(2)

                        if (LA15_1 == 47) :
                            alt15 = 2
                        elif ((0 <= LA15_1 <= 46) or (48 <= LA15_1 <= 65535)) :
                            alt15 = 1


                    elif ((0 <= LA15_0 <= 41) or (43 <= LA15_0 <= 65535)) :
                        alt15 = 1


                    if alt15 == 1:
                        # Imp.g:302:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop15


                self.match("*/")


                #action start
                _channel=HIDDEN;
                #action end



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Imp.g:305:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # Imp.g:305:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "ML_STRING"
    def mML_STRING(self, ):
        try:
            _type = ML_STRING
            _channel = DEFAULT_CHANNEL

            # Imp.g:313:5: ( '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' )
            # Imp.g:313:9: '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"'
            pass 
            self.match("\"\"\"")


            # Imp.g:313:15: ( options {greedy=false; } : . )*
            while True: #loop17
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 34) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == 34) :
                        LA17_3 = self.input.LA(3)

                        if (LA17_3 == 34) :
                            alt17 = 2
                        elif ((0 <= LA17_3 <= 33) or (35 <= LA17_3 <= 65535)) :
                            alt17 = 1


                    elif ((0 <= LA17_1 <= 33) or (35 <= LA17_1 <= 65535)) :
                        alt17 = 1


                elif ((0 <= LA17_0 <= 33) or (35 <= LA17_0 <= 65535)) :
                    alt17 = 1


                if alt17 == 1:
                    # Imp.g:313:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop17


            self.match("\"\"\"")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ML_STRING"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # Imp.g:317:5: ( '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"' )
            # Imp.g:317:9: '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)

            # Imp.g:317:13: ( ESC_SEQ |~ ( '\\\\' | '\"' ) )*
            while True: #loop18
                alt18 = 3
                LA18_0 = self.input.LA(1)

                if (LA18_0 == 92) :
                    alt18 = 1
                elif ((0 <= LA18_0 <= 33) or (35 <= LA18_0 <= 91) or (93 <= LA18_0 <= 65535)) :
                    alt18 = 2


                if alt18 == 1:
                    # Imp.g:317:15: ESC_SEQ
                    pass 
                    self.mESC_SEQ()



                elif alt18 == 2:
                    # Imp.g:317:25: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop18


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "REGEX"
    def mREGEX(self, ):
        try:
            _type = REGEX
            _channel = DEFAULT_CHANNEL

            # Imp.g:321:2: ( '/' (~ ( '/' ) )* '/' )
            # Imp.g:321:4: '/' (~ ( '/' ) )* '/'
            pass 
            self.match(47)

            # Imp.g:321:8: (~ ( '/' ) )*
            while True: #loop19
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((0 <= LA19_0 <= 46) or (48 <= LA19_0 <= 65535)) :
                    alt19 = 1


                if alt19 == 1:
                    # Imp.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop19


            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REGEX"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # Imp.g:326:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # Imp.g:326:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # Imp.g:326:22: ( '+' | '-' )?
            alt20 = 2
            LA20_0 = self.input.LA(1)

            if (LA20_0 == 43 or LA20_0 == 45) :
                alt20 = 1
            if alt20 == 1:
                # Imp.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # Imp.g:326:33: ( '0' .. '9' )+
            cnt21 = 0
            while True: #loop21
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((48 <= LA21_0 <= 57)) :
                    alt21 = 1


                if alt21 == 1:
                    # Imp.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt21 >= 1:
                        break #loop21

                    eee = EarlyExitException(21, self.input)
                    raise eee

                cnt21 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # Imp.g:329:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # Imp.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):
        try:
            # Imp.g:333:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt22 = 3
            LA22_0 = self.input.LA(1)

            if (LA22_0 == 92) :
                LA22 = self.input.LA(2)
                if LA22 in {34, 39, 92, 98, 102, 110, 114, 116}:
                    alt22 = 1
                elif LA22 in {117}:
                    alt22 = 2
                elif LA22 in {48, 49, 50, 51, 52, 53, 54, 55}:
                    alt22 = 3
                else:
                    nvae = NoViableAltException("", 22, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 22, 0, self.input)

                raise nvae


            if alt22 == 1:
                # Imp.g:333:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)

                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt22 == 2:
                # Imp.g:334:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()



            elif alt22 == 3:
                # Imp.g:335:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()




        finally:
            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):
        try:
            # Imp.g:340:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt23 = 3
            LA23_0 = self.input.LA(1)

            if (LA23_0 == 92) :
                LA23_1 = self.input.LA(2)

                if ((48 <= LA23_1 <= 51)) :
                    LA23_2 = self.input.LA(3)

                    if ((48 <= LA23_2 <= 55)) :
                        LA23_4 = self.input.LA(4)

                        if ((48 <= LA23_4 <= 55)) :
                            alt23 = 1
                        else:
                            alt23 = 2

                    else:
                        alt23 = 3

                elif ((52 <= LA23_1 <= 55)) :
                    LA23_3 = self.input.LA(3)

                    if ((48 <= LA23_3 <= 55)) :
                        alt23 = 2
                    else:
                        alt23 = 3

                else:
                    nvae = NoViableAltException("", 23, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 23, 0, self.input)

                raise nvae


            if alt23 == 1:
                # Imp.g:340:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 51):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt23 == 2:
                # Imp.g:341:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt23 == 3:
                # Imp.g:342:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





        finally:
            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):
        try:
            # Imp.g:347:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # Imp.g:347:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)

            self.match(117)

            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()





        finally:
            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # Imp.g:1:8: ( T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | ENUM_KEY | TRUE | FALSE | ID | CLASS_ID | INT | FLOAT | COMMENT | WS | ML_STRING | STRING | REGEX )
        alt24 = 54
        alt24 = self.dfa24.predict(self.input)
        if alt24 == 1:
            # Imp.g:1:10: T__50
            pass 
            self.mT__50()



        elif alt24 == 2:
            # Imp.g:1:16: T__51
            pass 
            self.mT__51()



        elif alt24 == 3:
            # Imp.g:1:22: T__52
            pass 
            self.mT__52()



        elif alt24 == 4:
            # Imp.g:1:28: T__53
            pass 
            self.mT__53()



        elif alt24 == 5:
            # Imp.g:1:34: T__54
            pass 
            self.mT__54()



        elif alt24 == 6:
            # Imp.g:1:40: T__55
            pass 
            self.mT__55()



        elif alt24 == 7:
            # Imp.g:1:46: T__56
            pass 
            self.mT__56()



        elif alt24 == 8:
            # Imp.g:1:52: T__57
            pass 
            self.mT__57()



        elif alt24 == 9:
            # Imp.g:1:58: T__58
            pass 
            self.mT__58()



        elif alt24 == 10:
            # Imp.g:1:64: T__59
            pass 
            self.mT__59()



        elif alt24 == 11:
            # Imp.g:1:70: T__60
            pass 
            self.mT__60()



        elif alt24 == 12:
            # Imp.g:1:76: T__61
            pass 
            self.mT__61()



        elif alt24 == 13:
            # Imp.g:1:82: T__62
            pass 
            self.mT__62()



        elif alt24 == 14:
            # Imp.g:1:88: T__63
            pass 
            self.mT__63()



        elif alt24 == 15:
            # Imp.g:1:94: T__64
            pass 
            self.mT__64()



        elif alt24 == 16:
            # Imp.g:1:100: T__65
            pass 
            self.mT__65()



        elif alt24 == 17:
            # Imp.g:1:106: T__66
            pass 
            self.mT__66()



        elif alt24 == 18:
            # Imp.g:1:112: T__67
            pass 
            self.mT__67()



        elif alt24 == 19:
            # Imp.g:1:118: T__68
            pass 
            self.mT__68()



        elif alt24 == 20:
            # Imp.g:1:124: T__69
            pass 
            self.mT__69()



        elif alt24 == 21:
            # Imp.g:1:130: T__70
            pass 
            self.mT__70()



        elif alt24 == 22:
            # Imp.g:1:136: T__71
            pass 
            self.mT__71()



        elif alt24 == 23:
            # Imp.g:1:142: T__72
            pass 
            self.mT__72()



        elif alt24 == 24:
            # Imp.g:1:148: T__73
            pass 
            self.mT__73()



        elif alt24 == 25:
            # Imp.g:1:154: T__74
            pass 
            self.mT__74()



        elif alt24 == 26:
            # Imp.g:1:160: T__75
            pass 
            self.mT__75()



        elif alt24 == 27:
            # Imp.g:1:166: T__76
            pass 
            self.mT__76()



        elif alt24 == 28:
            # Imp.g:1:172: T__77
            pass 
            self.mT__77()



        elif alt24 == 29:
            # Imp.g:1:178: T__78
            pass 
            self.mT__78()



        elif alt24 == 30:
            # Imp.g:1:184: T__79
            pass 
            self.mT__79()



        elif alt24 == 31:
            # Imp.g:1:190: T__80
            pass 
            self.mT__80()



        elif alt24 == 32:
            # Imp.g:1:196: T__81
            pass 
            self.mT__81()



        elif alt24 == 33:
            # Imp.g:1:202: T__82
            pass 
            self.mT__82()



        elif alt24 == 34:
            # Imp.g:1:208: T__83
            pass 
            self.mT__83()



        elif alt24 == 35:
            # Imp.g:1:214: T__84
            pass 
            self.mT__84()



        elif alt24 == 36:
            # Imp.g:1:220: T__85
            pass 
            self.mT__85()



        elif alt24 == 37:
            # Imp.g:1:226: T__86
            pass 
            self.mT__86()



        elif alt24 == 38:
            # Imp.g:1:232: T__87
            pass 
            self.mT__87()



        elif alt24 == 39:
            # Imp.g:1:238: T__88
            pass 
            self.mT__88()



        elif alt24 == 40:
            # Imp.g:1:244: T__89
            pass 
            self.mT__89()



        elif alt24 == 41:
            # Imp.g:1:250: T__90
            pass 
            self.mT__90()



        elif alt24 == 42:
            # Imp.g:1:256: T__91
            pass 
            self.mT__91()



        elif alt24 == 43:
            # Imp.g:1:262: ENUM_KEY
            pass 
            self.mENUM_KEY()



        elif alt24 == 44:
            # Imp.g:1:271: TRUE
            pass 
            self.mTRUE()



        elif alt24 == 45:
            # Imp.g:1:276: FALSE
            pass 
            self.mFALSE()



        elif alt24 == 46:
            # Imp.g:1:282: ID
            pass 
            self.mID()



        elif alt24 == 47:
            # Imp.g:1:285: CLASS_ID
            pass 
            self.mCLASS_ID()



        elif alt24 == 48:
            # Imp.g:1:294: INT
            pass 
            self.mINT()



        elif alt24 == 49:
            # Imp.g:1:298: FLOAT
            pass 
            self.mFLOAT()



        elif alt24 == 50:
            # Imp.g:1:304: COMMENT
            pass 
            self.mCOMMENT()



        elif alt24 == 51:
            # Imp.g:1:312: WS
            pass 
            self.mWS()



        elif alt24 == 52:
            # Imp.g:1:315: ML_STRING
            pass 
            self.mML_STRING()



        elif alt24 == 53:
            # Imp.g:1:325: STRING
            pass 
            self.mSTRING()



        elif alt24 == 54:
            # Imp.g:1:332: REGEX
            pass 
            self.mREGEX()








    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        "\5\uffff"
        )

    DFA10_eof = DFA.unpack(
        "\5\uffff"
        )

    DFA10_min = DFA.unpack(
        "\2\56\3\uffff"
        )

    DFA10_max = DFA.unpack(
        "\1\71\1\145\3\uffff"
        )

    DFA10_accept = DFA.unpack(
        "\2\uffff\1\2\1\1\1\3"
        )

    DFA10_special = DFA.unpack(
        "\5\uffff"
        )


    DFA10_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #24

    DFA24_eot = DFA.unpack(
        "\6\uffff\1\45\1\50\1\53\1\55\1\57\2\uffff\14\34\5\uffff\1\103\21"
        "\uffff\1\34\1\112\5\34\1\124\1\125\2\34\1\130\7\34\1\uffff\1\106"
        "\2\uffff\1\110\1\uffff\1\144\1\uffff\1\145\3\34\1\151\4\34\2\uffff"
        "\1\34\1\157\1\uffff\7\34\1\uffff\1\106\4\uffff\1\34\1\171\1\34\1"
        "\uffff\5\34\1\uffff\1\34\1\u0081\1\34\1\u0083\1\34\1\u0085\1\u0086"
        "\1\uffff\1\34\1\uffff\1\34\1\u0089\2\34\1\u008c\2\34\1\uffff\1\34"
        "\1\uffff\1\u0090\2\uffff\1\u0091\1\34\1\uffff\2\34\1\uffff\1\34"
        "\1\u0096\1\34\2\uffff\1\u0098\1\34\1\u009a\1\34\1\uffff\1\u009c"
        "\1\uffff\1\34\1\uffff\1\u009e\1\uffff\1\u00a0\1\uffff\1\34\1\uffff"
        "\3\34\1\u00a5\1\uffff"
        )

    DFA24_eof = DFA.unpack(
        "\u00a6\uffff"
        )

    DFA24_min = DFA.unpack(
        "\1\11\4\uffff\1\55\1\60\1\72\1\55\2\75\2\uffff\2\156\1\141\1\155"
        "\1\141\1\157\1\162\1\141\1\157\1\162\1\163\1\150\5\uffff\1\56\1"
        "\0\2\uffff\1\0\15\uffff\1\144\1\55\1\144\1\164\1\162\1\154\1\160"
        "\2\55\2\164\1\55\1\162\1\157\1\160\1\165\1\151\1\145\1\164\1\uffff"
        "\2\0\1\uffff\1\42\1\uffff\1\55\1\uffff\1\55\1\151\1\155\1\145\1"
        "\55\1\163\2\154\1\145\2\uffff\1\143\1\55\1\uffff\1\145\1\164\2\145"
        "\2\156\1\150\3\0\3\uffff\1\164\1\55\1\156\1\uffff\2\145\1\165\1"
        "\170\1\150\1\uffff\1\156\1\55\1\144\1\55\1\147\2\55\1\uffff\1\171"
        "\1\uffff\1\144\1\55\1\155\1\144\1\55\1\151\1\164\1\uffff\1\145\1"
        "\uffff\1\55\2\uffff\1\55\1\163\1\uffff\2\145\1\uffff\1\156\1\55"
        "\1\146\2\uffff\1\55\1\156\1\55\1\147\1\uffff\1\55\1\uffff\1\164"
        "\1\uffff\1\55\1\uffff\1\55\1\uffff\1\164\1\uffff\1\151\1\157\1\156"
        "\1\55\1\uffff"
        )

    DFA24_max = DFA.unpack(
        "\1\175\4\uffff\1\76\1\71\1\72\3\75\2\uffff\1\163\1\170\1\157\1\163"
        "\1\141\1\157\1\162\1\141\1\157\1\171\1\163\1\151\5\uffff\1\145\1"
        "\uffff\2\uffff\1\uffff\15\uffff\1\144\1\172\1\165\1\164\1\162\1"
        "\154\1\160\2\172\2\164\1\172\1\162\1\157\1\160\1\165\1\151\1\145"
        "\1\164\1\uffff\2\uffff\1\uffff\1\42\1\uffff\1\172\1\uffff\1\172"
        "\1\151\1\155\1\145\1\172\1\163\2\154\1\145\2\uffff\1\143\1\172\1"
        "\uffff\1\145\1\164\2\145\2\156\1\150\3\uffff\3\uffff\1\164\1\172"
        "\1\156\1\uffff\2\145\1\165\1\170\1\150\1\uffff\1\156\1\172\1\144"
        "\1\172\1\147\2\172\1\uffff\1\171\1\uffff\1\144\1\172\1\155\1\144"
        "\1\172\1\151\1\164\1\uffff\1\145\1\uffff\1\172\2\uffff\1\172\1\163"
        "\1\uffff\2\145\1\uffff\1\156\1\172\1\146\2\uffff\1\172\1\156\1\172"
        "\1\147\1\uffff\1\172\1\uffff\1\164\1\uffff\1\172\1\uffff\1\172\1"
        "\uffff\1\164\1\uffff\1\151\1\157\1\156\1\172\1\uffff"
        )

    DFA24_accept = DFA.unpack(
        "\1\uffff\1\1\1\2\1\3\1\4\6\uffff\1\21\1\22\14\uffff\1\50\1\51\1"
        "\52\1\56\1\57\2\uffff\1\62\1\63\1\uffff\1\5\1\6\1\7\1\61\1\11\1"
        "\10\1\13\1\14\1\12\1\16\1\15\1\20\1\17\23\uffff\1\60\2\uffff\1\66"
        "\1\uffff\1\65\1\uffff\1\24\11\uffff\1\33\1\36\2\uffff\1\41\12\uffff"
        "\1\64\1\23\1\25\3\uffff\1\30\5\uffff\1\40\7\uffff\1\62\1\uffff\1"
        "\53\7\uffff\1\43\1\uffff\1\54\1\uffff\1\46\1\47\2\uffff\1\55\2\uffff"
        "\1\35\3\uffff\1\45\1\26\4\uffff\1\42\1\uffff\1\27\1\uffff\1\34\1"
        "\uffff\1\44\1\uffff\1\37\1\uffff\1\31\4\uffff\1\32"
        )

    DFA24_special = DFA.unpack(
        "\37\uffff\1\2\2\uffff\1\4\41\uffff\1\5\1\3\32\uffff\1\1\1\6\1\0"
        "\103\uffff"
        )


    DFA24_transition = [
        DFA.unpack("\2\41\2\uffff\1\41\22\uffff\1\41\1\1\1\42\1\40\4\uffff"
        "\1\2\1\3\2\uffff\1\4\1\5\1\6\1\37\12\36\1\7\1\uffff\1\10\1\11\1"
        "\12\2\uffff\32\35\1\13\1\uffff\1\14\1\uffff\1\34\1\uffff\1\15\3"
        "\34\1\16\1\17\2\34\1\20\3\34\1\21\1\22\1\23\1\24\1\34\1\25\1\34"
        "\1\26\1\27\1\34\1\30\3\34\1\31\1\32\1\33"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\43\20\uffff\1\44"),
        DFA.unpack("\12\46"),
        DFA.unpack("\1\47"),
        DFA.unpack("\1\51\17\uffff\1\52"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\56"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\60\4\uffff\1\61"),
        DFA.unpack("\1\62\11\uffff\1\63"),
        DFA.unpack("\1\65\15\uffff\1\64"),
        DFA.unpack("\1\66\1\67\4\uffff\1\70"),
        DFA.unpack("\1\71"),
        DFA.unpack("\1\72"),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\74"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\77\6\uffff\1\76"),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101\1\102"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\46\1\uffff\12\36\13\uffff\1\46\37\uffff\1\46"),
        DFA.unpack("\52\106\1\105\4\106\1\104\uffd0\106"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\42\110\1\107\uffdd\110"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\113\17\uffff\1\114\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\2\34\1\122\1\123\26\34"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\131"),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack(""),
        DFA.unpack("\0\40"),
        DFA.unpack("\52\142\1\140\4\142\1\141\uffd0\142"),
        DFA.unpack(""),
        DFA.unpack("\1\143"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack("\52\142\1\140\4\142\1\167\uffd0\142"),
        DFA.unpack("\0\40"),
        DFA.unpack("\52\142\1\140\4\142\1\141\uffd0\142"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\172"),
        DFA.unpack(""),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack(""),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack("\1\u0087"),
        DFA.unpack(""),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
        DFA.unpack("\1\u008f"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u0092"),
        DFA.unpack(""),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack(""),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u0097"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("\1\u009b"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack("\1\u009d"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack(""),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\1\u009f\31\34"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a1"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff\1\34\1\uffff"
        "\32\34"),
        DFA.unpack("")
    ]

    # class definition for DFA #24

    class DFA24(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA24_98 = input.LA(1)

                s = -1
                if (LA24_98 == 42):
                    s = 96

                elif (LA24_98 == 47):
                    s = 97

                elif ((0 <= LA24_98 <= 41) or (43 <= LA24_98 <= 46) or (48 <= LA24_98 <= 65535)):
                    s = 98

                if s >= 0:
                    return s
            elif s == 1: 
                LA24_96 = input.LA(1)

                s = -1
                if (LA24_96 == 47):
                    s = 119

                elif (LA24_96 == 42):
                    s = 96

                elif ((0 <= LA24_96 <= 41) or (43 <= LA24_96 <= 46) or (48 <= LA24_96 <= 65535)):
                    s = 98

                if s >= 0:
                    return s
            elif s == 2: 
                LA24_31 = input.LA(1)

                s = -1
                if (LA24_31 == 47):
                    s = 68

                elif (LA24_31 == 42):
                    s = 69

                elif ((0 <= LA24_31 <= 41) or (43 <= LA24_31 <= 46) or (48 <= LA24_31 <= 65535)):
                    s = 70

                if s >= 0:
                    return s
            elif s == 3: 
                LA24_69 = input.LA(1)

                s = -1
                if (LA24_69 == 42):
                    s = 96

                elif (LA24_69 == 47):
                    s = 97

                elif ((0 <= LA24_69 <= 41) or (43 <= LA24_69 <= 46) or (48 <= LA24_69 <= 65535)):
                    s = 98

                if s >= 0:
                    return s
            elif s == 4: 
                LA24_34 = input.LA(1)

                s = -1
                if (LA24_34 == 34):
                    s = 71

                elif ((0 <= LA24_34 <= 33) or (35 <= LA24_34 <= 65535)):
                    s = 72

                if s >= 0:
                    return s
            elif s == 5: 
                LA24_68 = input.LA(1)

                s = -1
                if ((0 <= LA24_68 <= 65535)):
                    s = 32

                else:
                    s = 70

                if s >= 0:
                    return s
            elif s == 6: 
                LA24_97 = input.LA(1)

                s = -1
                if ((0 <= LA24_97 <= 65535)):
                    s = 32

                else:
                    s = 70

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 24, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from Imp.antlr3.main import LexerMain
    main = LexerMain(ImpLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
