# $ANTLR 3.4.1-SNAPSHOT Imp.g 2013-12-03 11:46:21

import sys
from Imp.antlr3 import *

from Imp.antlr3.tree import *




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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ANON", "ASSIGN", "ATTR", "CALL", "CLASS_ID", "CLASS_REF", "COMMENT", 
    "CONSTRUCT", "DEF_DEFAULT", "DEF_ENTITY", "DEF_IMPLEMENT", "DEF_IMPLEMENTATION", 
    "DEF_RELATION", "DEF_TYPE", "ENUM", "ENUM_KEY", "ESC_SEQ", "EXPONENT", 
    "EXPRESSION", "FALSE", "FLOAT", "FOR", "HASH", "HEX_DIGIT", "ID", "INCLUDE", 
    "INDEX", "INT", "LAMBDA", "LIST", "METHOD", "ML_STRING", "MULT", "NONE", 
    "NS", "OCTAL_ESC", "OP", "ORPHAN", "REF", "REGEX", "STATEMENT", "STRING", 
    "TRUE", "UNICODE_ESC", "VAR_REF", "WS", "'!='", "'('", "')'", "','", 
    "'--'", "'->'", "'.'", "':'", "'::'", "'<'", "'<-'", "'<='", "'='", 
    "'=='", "'>'", "'>='", "'['", "']'", "'and'", "'as'", "'end'", "'entity'", 
    "'extends'", "'for'", "'implement'", "'implementation'", "'in'", "'include'", 
    "'index'", "'is'", "'matching'", "'not'", "'or'", "'parent'", "'root'", 
    "'typedef'", "'using'", "'when'", "'with'", "'{'", "'|'", "'}'"
]



class ImpParser(Parser):
    grammarFileName = "Imp.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)

        self.dfa1 = self.DFA1(
            self, 1,
            eot = self.DFA1_eot,
            eof = self.DFA1_eof,
            min = self.DFA1_min,
            max = self.DFA1_max,
            accept = self.DFA1_accept,
            special = self.DFA1_special,
            transition = self.DFA1_transition
            )

        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )

        self.dfa28 = self.DFA28(
            self, 28,
            eot = self.DFA28_eot,
            eof = self.DFA28_eof,
            min = self.DFA28_min,
            max = self.DFA28_max,
            accept = self.DFA28_accept,
            special = self.DFA28_special,
            transition = self.DFA28_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )

        self.dfa41 = self.DFA41(
            self, 41,
            eot = self.DFA41_eot,
            eof = self.DFA41_eof,
            min = self.DFA41_min,
            max = self.DFA41_max,
            accept = self.DFA41_accept,
            special = self.DFA41_special,
            transition = self.DFA41_transition
            )




        self.delegates = []

        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class main_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "main"
    # Imp.g:47:1: main : ( def_statement | top_statement | ML_STRING )* -> ^( LIST ( def_statement )* ( top_statement )* ( ML_STRING )* ) ;
    def main(self, ):
        retval = self.main_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ML_STRING3 = None
        def_statement1 = None
        top_statement2 = None

        ML_STRING3_tree = None
        stream_ML_STRING = RewriteRuleTokenStream(self._adaptor, "token ML_STRING")
        stream_def_statement = RewriteRuleSubtreeStream(self._adaptor, "rule def_statement")
        stream_top_statement = RewriteRuleSubtreeStream(self._adaptor, "rule top_statement")
        try:
            try:
                # Imp.g:48:2: ( ( def_statement | top_statement | ML_STRING )* -> ^( LIST ( def_statement )* ( top_statement )* ( ML_STRING )* ) )
                # Imp.g:48:4: ( def_statement | top_statement | ML_STRING )*
                pass 
                # Imp.g:48:4: ( def_statement | top_statement | ML_STRING )*
                while True: #loop1
                    alt1 = 4
                    alt1 = self.dfa1.predict(self.input)
                    if alt1 == 1:
                        # Imp.g:48:5: def_statement
                        pass 
                        self._state.following.append(self.FOLLOW_def_statement_in_main172)
                        def_statement1 = self.def_statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_def_statement.add(def_statement1.tree)



                    elif alt1 == 2:
                        # Imp.g:48:21: top_statement
                        pass 
                        self._state.following.append(self.FOLLOW_top_statement_in_main176)
                        top_statement2 = self.top_statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_top_statement.add(top_statement2.tree)



                    elif alt1 == 3:
                        # Imp.g:48:37: ML_STRING
                        pass 
                        ML_STRING3 = self.match(self.input, ML_STRING, self.FOLLOW_ML_STRING_in_main180) 
                        if self._state.backtracking == 0:
                            stream_ML_STRING.add(ML_STRING3)



                    else:
                        break #loop1


                # AST Rewrite
                # elements: top_statement, def_statement, ML_STRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 48:49: -> ^( LIST ( def_statement )* ( top_statement )* ( ML_STRING )* )
                    # Imp.g:48:52: ^( LIST ( def_statement )* ( top_statement )* ( ML_STRING )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # Imp.g:48:59: ( def_statement )*
                    while stream_def_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_def_statement.nextTree())


                    stream_def_statement.reset();

                    # Imp.g:48:74: ( top_statement )*
                    while stream_top_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_top_statement.nextTree())


                    stream_top_statement.reset();

                    # Imp.g:48:89: ( ML_STRING )*
                    while stream_ML_STRING.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ML_STRING.nextNode()
                        )


                    stream_ML_STRING.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "main"


    class def_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "def_statement"
    # Imp.g:51:1: def_statement : ( typedef | entity_def | implementation_def | relation | index | implement_def );
    def def_statement(self, ):
        retval = self.def_statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        typedef4 = None
        entity_def5 = None
        implementation_def6 = None
        relation7 = None
        index8 = None
        implement_def9 = None


        try:
            try:
                # Imp.g:52:2: ( typedef | entity_def | implementation_def | relation | index | implement_def )
                alt2 = 6
                LA2 = self.input.LA(1)
                if LA2 in {85}:
                    alt2 = 1
                elif LA2 in {71}:
                    alt2 = 2
                elif LA2 in {75}:
                    alt2 = 3
                elif LA2 in {CLASS_ID, ID}:
                    alt2 = 4
                elif LA2 in {78}:
                    alt2 = 5
                elif LA2 in {74}:
                    alt2 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # Imp.g:52:4: typedef
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_typedef_in_def_statement208)
                    typedef4 = self.typedef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typedef4.tree)



                elif alt2 == 2:
                    # Imp.g:52:14: entity_def
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_entity_def_in_def_statement212)
                    entity_def5 = self.entity_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, entity_def5.tree)



                elif alt2 == 3:
                    # Imp.g:52:27: implementation_def
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_implementation_def_in_def_statement216)
                    implementation_def6 = self.implementation_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, implementation_def6.tree)



                elif alt2 == 4:
                    # Imp.g:52:48: relation
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_relation_in_def_statement220)
                    relation7 = self.relation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, relation7.tree)



                elif alt2 == 5:
                    # Imp.g:52:59: index
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_index_in_def_statement224)
                    index8 = self.index()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, index8.tree)



                elif alt2 == 6:
                    # Imp.g:52:67: implement_def
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_implement_def_in_def_statement228)
                    implement_def9 = self.implement_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, implement_def9.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "def_statement"


    class index_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "index"
    # Imp.g:55:1: index : 'index' class_ref '(' ID ( ',' ID )* ')' -> ^( INDEX class_ref ^( LIST ( ID )+ ) ) ;
    def index(self, ):
        retval = self.index_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal10 = None
        char_literal12 = None
        ID13 = None
        char_literal14 = None
        ID15 = None
        char_literal16 = None
        class_ref11 = None

        string_literal10_tree = None
        char_literal12_tree = None
        ID13_tree = None
        char_literal14_tree = None
        ID15_tree = None
        char_literal16_tree = None
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        try:
            try:
                # Imp.g:56:2: ( 'index' class_ref '(' ID ( ',' ID )* ')' -> ^( INDEX class_ref ^( LIST ( ID )+ ) ) )
                # Imp.g:56:4: 'index' class_ref '(' ID ( ',' ID )* ')'
                pass 
                string_literal10 = self.match(self.input, 78, self.FOLLOW_78_in_index240) 
                if self._state.backtracking == 0:
                    stream_78.add(string_literal10)


                self._state.following.append(self.FOLLOW_class_ref_in_index242)
                class_ref11 = self.class_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_class_ref.add(class_ref11.tree)


                char_literal12 = self.match(self.input, 51, self.FOLLOW_51_in_index244) 
                if self._state.backtracking == 0:
                    stream_51.add(char_literal12)


                ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_index246) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID13)


                # Imp.g:56:29: ( ',' ID )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 53) :
                        alt3 = 1


                    if alt3 == 1:
                        # Imp.g:56:30: ',' ID
                        pass 
                        char_literal14 = self.match(self.input, 53, self.FOLLOW_53_in_index249) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal14)


                        ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_index251) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID15)



                    else:
                        break #loop3


                char_literal16 = self.match(self.input, 52, self.FOLLOW_52_in_index255) 
                if self._state.backtracking == 0:
                    stream_52.add(char_literal16)


                # AST Rewrite
                # elements: ID, class_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 56:43: -> ^( INDEX class_ref ^( LIST ( ID )+ ) )
                    # Imp.g:56:46: ^( INDEX class_ref ^( LIST ( ID )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(INDEX, "INDEX")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_class_ref.nextTree())

                    # Imp.g:56:64: ^( LIST ( ID )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    # Imp.g:56:71: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_2, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "index"


    class rhs_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "rhs"
    # Imp.g:59:1: rhs : ( ( class_ref '(' )=> anon_ctor | operand );
    def rhs(self, ):
        retval = self.rhs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        anon_ctor17 = None
        operand18 = None


        try:
            try:
                # Imp.g:60:2: ( ( class_ref '(' )=> anon_ctor | operand )
                alt4 = 2
                alt4 = self.dfa4.predict(self.input)
                if alt4 == 1:
                    # Imp.g:60:4: ( class_ref '(' )=> anon_ctor
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_anon_ctor_in_rhs291)
                    anon_ctor17 = self.anon_ctor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, anon_ctor17.tree)



                elif alt4 == 2:
                    # Imp.g:61:4: operand
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_operand_in_rhs296)
                    operand18 = self.operand()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, operand18.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "rhs"


    class top_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "top_statement"
    # Imp.g:64:1: top_statement : ( 'include' ns_ref -> ^( INCLUDE ns_ref ) | ( 'for' )=> 'for' ID 'in' ( variable | class_ref ) implementation -> ^( FOR ID ( variable )? ( class_ref )? implementation ) | variable '=' rhs -> ^( ASSIGN variable rhs ) | ( class_ref '(' )=> anon_ctor -> ^( ORPHAN anon_ctor ) | function_call | method_call | enum_stmt );
    def top_statement(self, ):
        retval = self.top_statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal19 = None
        string_literal21 = None
        ID22 = None
        string_literal23 = None
        char_literal28 = None
        ns_ref20 = None
        variable24 = None
        class_ref25 = None
        implementation26 = None
        variable27 = None
        rhs29 = None
        anon_ctor30 = None
        function_call31 = None
        method_call32 = None
        enum_stmt33 = None

        string_literal19_tree = None
        string_literal21_tree = None
        ID22_tree = None
        string_literal23_tree = None
        char_literal28_tree = None
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_anon_ctor = RewriteRuleSubtreeStream(self._adaptor, "rule anon_ctor")
        stream_implementation = RewriteRuleSubtreeStream(self._adaptor, "rule implementation")
        stream_rhs = RewriteRuleSubtreeStream(self._adaptor, "rule rhs")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        stream_variable = RewriteRuleSubtreeStream(self._adaptor, "rule variable")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:66:2: ( 'include' ns_ref -> ^( INCLUDE ns_ref ) | ( 'for' )=> 'for' ID 'in' ( variable | class_ref ) implementation -> ^( FOR ID ( variable )? ( class_ref )? implementation ) | variable '=' rhs -> ^( ASSIGN variable rhs ) | ( class_ref '(' )=> anon_ctor -> ^( ORPHAN anon_ctor ) | function_call | method_call | enum_stmt )
                alt6 = 7
                alt6 = self.dfa6.predict(self.input)
                if alt6 == 1:
                    # Imp.g:66:4: 'include' ns_ref
                    pass 
                    string_literal19 = self.match(self.input, 77, self.FOLLOW_77_in_top_statement309) 
                    if self._state.backtracking == 0:
                        stream_77.add(string_literal19)


                    self._state.following.append(self.FOLLOW_ns_ref_in_top_statement311)
                    ns_ref20 = self.ns_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_ns_ref.add(ns_ref20.tree)


                    # AST Rewrite
                    # elements: ns_ref
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 66:21: -> ^( INCLUDE ns_ref )
                        # Imp.g:66:24: ^( INCLUDE ns_ref )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(INCLUDE, "INCLUDE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_ns_ref.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 2:
                    # Imp.g:67:4: ( 'for' )=> 'for' ID 'in' ( variable | class_ref ) implementation
                    pass 
                    string_literal21 = self.match(self.input, 73, self.FOLLOW_73_in_top_statement331) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal21)


                    ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_top_statement333) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID22)


                    string_literal23 = self.match(self.input, 76, self.FOLLOW_76_in_top_statement335) 
                    if self._state.backtracking == 0:
                        stream_76.add(string_literal23)


                    # Imp.g:67:29: ( variable | class_ref )
                    alt5 = 2
                    alt5 = self.dfa5.predict(self.input)
                    if alt5 == 1:
                        # Imp.g:67:30: variable
                        pass 
                        self._state.following.append(self.FOLLOW_variable_in_top_statement338)
                        variable24 = self.variable()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_variable.add(variable24.tree)



                    elif alt5 == 2:
                        # Imp.g:67:41: class_ref
                        pass 
                        self._state.following.append(self.FOLLOW_class_ref_in_top_statement342)
                        class_ref25 = self.class_ref()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_class_ref.add(class_ref25.tree)





                    self._state.following.append(self.FOLLOW_implementation_in_top_statement346)
                    implementation26 = self.implementation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementation.add(implementation26.tree)


                    # AST Rewrite
                    # elements: ID, implementation, variable, class_ref
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 67:68: -> ^( FOR ID ( variable )? ( class_ref )? implementation )
                        # Imp.g:67:71: ^( FOR ID ( variable )? ( class_ref )? implementation )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(FOR, "FOR")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )

                        # Imp.g:67:80: ( variable )?
                        if stream_variable.hasNext():
                            self._adaptor.addChild(root_1, stream_variable.nextTree())


                        stream_variable.reset();

                        # Imp.g:67:90: ( class_ref )?
                        if stream_class_ref.hasNext():
                            self._adaptor.addChild(root_1, stream_class_ref.nextTree())


                        stream_class_ref.reset();

                        self._adaptor.addChild(root_1, stream_implementation.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 3:
                    # Imp.g:68:4: variable '=' rhs
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_top_statement367)
                    variable27 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variable.add(variable27.tree)


                    char_literal28 = self.match(self.input, 62, self.FOLLOW_62_in_top_statement369) 
                    if self._state.backtracking == 0:
                        stream_62.add(char_literal28)


                    self._state.following.append(self.FOLLOW_rhs_in_top_statement371)
                    rhs29 = self.rhs()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rhs.add(rhs29.tree)


                    # AST Rewrite
                    # elements: variable, rhs
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 68:21: -> ^( ASSIGN variable rhs )
                        # Imp.g:68:24: ^( ASSIGN variable rhs )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ASSIGN, "ASSIGN")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_variable.nextTree())

                        self._adaptor.addChild(root_1, stream_rhs.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 4:
                    # Imp.g:69:4: ( class_ref '(' )=> anon_ctor
                    pass 
                    self._state.following.append(self.FOLLOW_anon_ctor_in_top_statement394)
                    anon_ctor30 = self.anon_ctor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_anon_ctor.add(anon_ctor30.tree)


                    # AST Rewrite
                    # elements: anon_ctor
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 69:33: -> ^( ORPHAN anon_ctor )
                        # Imp.g:69:36: ^( ORPHAN anon_ctor )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ORPHAN, "ORPHAN")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_anon_ctor.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt6 == 5:
                    # Imp.g:70:4: function_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_function_call_in_top_statement407)
                    function_call31 = self.function_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function_call31.tree)



                elif alt6 == 6:
                    # Imp.g:71:4: method_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_method_call_in_top_statement412)
                    method_call32 = self.method_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, method_call32.tree)



                elif alt6 == 7:
                    # Imp.g:72:4: enum_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_enum_stmt_in_top_statement417)
                    enum_stmt33 = self.enum_stmt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, enum_stmt33.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "top_statement"


    class enum_parent_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "enum_parent"
    # Imp.g:75:1: enum_parent : ( STRING | 'root' );
    def enum_parent(self, ):
        retval = self.enum_parent_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set34 = None

        set34_tree = None

        try:
            try:
                # Imp.g:76:2: ( STRING | 'root' )
                # Imp.g:
                pass 
                root_0 = self._adaptor.nil()


                set34 = self.input.LT(1)

                if self.input.LA(1) == STRING or self.input.LA(1) == 84:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set34))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "enum_parent"


    class enum_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "enum_stmt"
    # Imp.g:79:1: enum_stmt : ENUM_KEY ns_ref 'with' 'parent' enum_parent 'as' STRING ( ',' STRING )* -> ^( ENUM ns_ref ^( enum_parent ( STRING )+ ) ) ;
    def enum_stmt(self, ):
        retval = self.enum_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ENUM_KEY35 = None
        string_literal37 = None
        string_literal38 = None
        string_literal40 = None
        STRING41 = None
        char_literal42 = None
        STRING43 = None
        ns_ref36 = None
        enum_parent39 = None

        ENUM_KEY35_tree = None
        string_literal37_tree = None
        string_literal38_tree = None
        string_literal40_tree = None
        STRING41_tree = None
        char_literal42_tree = None
        STRING43_tree = None
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_83 = RewriteRuleTokenStream(self._adaptor, "token 83")
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_88 = RewriteRuleTokenStream(self._adaptor, "token 88")
        stream_ENUM_KEY = RewriteRuleTokenStream(self._adaptor, "token ENUM_KEY")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")
        stream_enum_parent = RewriteRuleSubtreeStream(self._adaptor, "rule enum_parent")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:80:2: ( ENUM_KEY ns_ref 'with' 'parent' enum_parent 'as' STRING ( ',' STRING )* -> ^( ENUM ns_ref ^( enum_parent ( STRING )+ ) ) )
                # Imp.g:80:4: ENUM_KEY ns_ref 'with' 'parent' enum_parent 'as' STRING ( ',' STRING )*
                pass 
                ENUM_KEY35 = self.match(self.input, ENUM_KEY, self.FOLLOW_ENUM_KEY_in_enum_stmt445) 
                if self._state.backtracking == 0:
                    stream_ENUM_KEY.add(ENUM_KEY35)


                self._state.following.append(self.FOLLOW_ns_ref_in_enum_stmt447)
                ns_ref36 = self.ns_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_ns_ref.add(ns_ref36.tree)


                string_literal37 = self.match(self.input, 88, self.FOLLOW_88_in_enum_stmt449) 
                if self._state.backtracking == 0:
                    stream_88.add(string_literal37)


                string_literal38 = self.match(self.input, 83, self.FOLLOW_83_in_enum_stmt451) 
                if self._state.backtracking == 0:
                    stream_83.add(string_literal38)


                self._state.following.append(self.FOLLOW_enum_parent_in_enum_stmt453)
                enum_parent39 = self.enum_parent()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_enum_parent.add(enum_parent39.tree)


                string_literal40 = self.match(self.input, 69, self.FOLLOW_69_in_enum_stmt455) 
                if self._state.backtracking == 0:
                    stream_69.add(string_literal40)


                STRING41 = self.match(self.input, STRING, self.FOLLOW_STRING_in_enum_stmt457) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING41)


                # Imp.g:80:60: ( ',' STRING )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 53) :
                        alt7 = 1


                    if alt7 == 1:
                        # Imp.g:80:61: ',' STRING
                        pass 
                        char_literal42 = self.match(self.input, 53, self.FOLLOW_53_in_enum_stmt460) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal42)


                        STRING43 = self.match(self.input, STRING, self.FOLLOW_STRING_in_enum_stmt462) 
                        if self._state.backtracking == 0:
                            stream_STRING.add(STRING43)



                    else:
                        break #loop7


                # AST Rewrite
                # elements: enum_parent, STRING, ns_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 80:74: -> ^( ENUM ns_ref ^( enum_parent ( STRING )+ ) )
                    # Imp.g:80:77: ^( ENUM ns_ref ^( enum_parent ( STRING )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ENUM, "ENUM")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_ns_ref.nextTree())

                    # Imp.g:80:91: ^( enum_parent ( STRING )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(stream_enum_parent.nextNode(), root_2)

                    # Imp.g:80:105: ( STRING )+
                    if not (stream_STRING.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_STRING.hasNext():
                        self._adaptor.addChild(root_2, 
                        stream_STRING.nextNode()
                        )


                    stream_STRING.reset()

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "enum_stmt"


    class anon_ctor_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "anon_ctor"
    # Imp.g:83:1: anon_ctor : constructor ( implementation )? -> ^( ANON constructor ( implementation )? ) ;
    def anon_ctor(self, ):
        retval = self.anon_ctor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        constructor44 = None
        implementation45 = None

        stream_implementation = RewriteRuleSubtreeStream(self._adaptor, "rule implementation")
        stream_constructor = RewriteRuleSubtreeStream(self._adaptor, "rule constructor")
        try:
            try:
                # Imp.g:84:2: ( constructor ( implementation )? -> ^( ANON constructor ( implementation )? ) )
                # Imp.g:84:4: constructor ( implementation )?
                pass 
                self._state.following.append(self.FOLLOW_constructor_in_anon_ctor491)
                constructor44 = self.constructor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_constructor.add(constructor44.tree)


                # Imp.g:84:16: ( implementation )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 57) :
                    alt8 = 1
                if alt8 == 1:
                    # Imp.g:84:16: implementation
                    pass 
                    self._state.following.append(self.FOLLOW_implementation_in_anon_ctor493)
                    implementation45 = self.implementation()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_implementation.add(implementation45.tree)





                # AST Rewrite
                # elements: constructor, implementation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 84:32: -> ^( ANON constructor ( implementation )? )
                    # Imp.g:84:35: ^( ANON constructor ( implementation )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ANON, "ANON")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_constructor.nextTree())

                    # Imp.g:84:54: ( implementation )?
                    if stream_implementation.hasNext():
                        self._adaptor.addChild(root_1, stream_implementation.nextTree())


                    stream_implementation.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "anon_ctor"


    class lambda_ctor_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "lambda_ctor"
    # Imp.g:87:1: lambda_ctor : constructor -> ^( ORPHAN constructor ) ;
    def lambda_ctor(self, ):
        retval = self.lambda_ctor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        constructor46 = None

        stream_constructor = RewriteRuleSubtreeStream(self._adaptor, "rule constructor")
        try:
            try:
                # Imp.g:88:2: ( constructor -> ^( ORPHAN constructor ) )
                # Imp.g:88:4: constructor
                pass 
                self._state.following.append(self.FOLLOW_constructor_in_lambda_ctor517)
                constructor46 = self.constructor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_constructor.add(constructor46.tree)


                # AST Rewrite
                # elements: constructor
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 88:16: -> ^( ORPHAN constructor )
                    # Imp.g:88:19: ^( ORPHAN constructor )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ORPHAN, "ORPHAN")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_constructor.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "lambda_ctor"


    class lambda_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "lambda_func"
    # Imp.g:91:1: lambda_func : ID '|' ( function_call | method_call | lambda_ctor ) -> ^( LAMBDA ID ( function_call )? ( method_call )? ( lambda_ctor )? ) ;
    def lambda_func(self, ):
        retval = self.lambda_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID47 = None
        char_literal48 = None
        function_call49 = None
        method_call50 = None
        lambda_ctor51 = None

        ID47_tree = None
        char_literal48_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_lambda_ctor = RewriteRuleSubtreeStream(self._adaptor, "rule lambda_ctor")
        stream_function_call = RewriteRuleSubtreeStream(self._adaptor, "rule function_call")
        stream_method_call = RewriteRuleSubtreeStream(self._adaptor, "rule method_call")
        try:
            try:
                # Imp.g:92:2: ( ID '|' ( function_call | method_call | lambda_ctor ) -> ^( LAMBDA ID ( function_call )? ( method_call )? ( lambda_ctor )? ) )
                # Imp.g:92:4: ID '|' ( function_call | method_call | lambda_ctor )
                pass 
                ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_lambda_func537) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID47)


                char_literal48 = self.match(self.input, 90, self.FOLLOW_90_in_lambda_func539) 
                if self._state.backtracking == 0:
                    stream_90.add(char_literal48)


                # Imp.g:92:11: ( function_call | method_call | lambda_ctor )
                alt9 = 3
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # Imp.g:92:12: function_call
                    pass 
                    self._state.following.append(self.FOLLOW_function_call_in_lambda_func542)
                    function_call49 = self.function_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_call.add(function_call49.tree)



                elif alt9 == 2:
                    # Imp.g:92:28: method_call
                    pass 
                    self._state.following.append(self.FOLLOW_method_call_in_lambda_func546)
                    method_call50 = self.method_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_method_call.add(method_call50.tree)



                elif alt9 == 3:
                    # Imp.g:92:42: lambda_ctor
                    pass 
                    self._state.following.append(self.FOLLOW_lambda_ctor_in_lambda_func550)
                    lambda_ctor51 = self.lambda_ctor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_lambda_ctor.add(lambda_ctor51.tree)





                # AST Rewrite
                # elements: lambda_ctor, method_call, ID, function_call
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 92:55: -> ^( LAMBDA ID ( function_call )? ( method_call )? ( lambda_ctor )? )
                    # Imp.g:92:58: ^( LAMBDA ID ( function_call )? ( method_call )? ( lambda_ctor )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LAMBDA, "LAMBDA")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # Imp.g:92:70: ( function_call )?
                    if stream_function_call.hasNext():
                        self._adaptor.addChild(root_1, stream_function_call.nextTree())


                    stream_function_call.reset();

                    # Imp.g:92:85: ( method_call )?
                    if stream_method_call.hasNext():
                        self._adaptor.addChild(root_1, stream_method_call.nextTree())


                    stream_method_call.reset();

                    # Imp.g:92:98: ( lambda_ctor )?
                    if stream_lambda_ctor.hasNext():
                        self._adaptor.addChild(root_1, stream_lambda_ctor.nextTree())


                    stream_lambda_ctor.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "lambda_func"


    class implementation_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "implementation_def"
    # Imp.g:95:1: implementation_def : 'implementation' ID ( 'for' class_ref )? implementation -> ^( DEF_IMPLEMENTATION ID implementation ( class_ref )? ) ;
    def implementation_def(self, ):
        retval = self.implementation_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal52 = None
        ID53 = None
        string_literal54 = None
        class_ref55 = None
        implementation56 = None

        string_literal52_tree = None
        ID53_tree = None
        string_literal54_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_implementation = RewriteRuleSubtreeStream(self._adaptor, "rule implementation")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        try:
            try:
                # Imp.g:96:2: ( 'implementation' ID ( 'for' class_ref )? implementation -> ^( DEF_IMPLEMENTATION ID implementation ( class_ref )? ) )
                # Imp.g:96:4: 'implementation' ID ( 'for' class_ref )? implementation
                pass 
                string_literal52 = self.match(self.input, 75, self.FOLLOW_75_in_implementation_def579) 
                if self._state.backtracking == 0:
                    stream_75.add(string_literal52)


                ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_implementation_def581) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID53)


                # Imp.g:96:24: ( 'for' class_ref )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 73) :
                    alt10 = 1
                if alt10 == 1:
                    # Imp.g:96:25: 'for' class_ref
                    pass 
                    string_literal54 = self.match(self.input, 73, self.FOLLOW_73_in_implementation_def584) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal54)


                    self._state.following.append(self.FOLLOW_class_ref_in_implementation_def586)
                    class_ref55 = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_ref.add(class_ref55.tree)





                self._state.following.append(self.FOLLOW_implementation_in_implementation_def590)
                implementation56 = self.implementation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_implementation.add(implementation56.tree)


                # AST Rewrite
                # elements: ID, class_ref, implementation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 96:58: -> ^( DEF_IMPLEMENTATION ID implementation ( class_ref )? )
                    # Imp.g:96:61: ^( DEF_IMPLEMENTATION ID implementation ( class_ref )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DEF_IMPLEMENTATION, "DEF_IMPLEMENTATION")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_implementation.nextTree())

                    # Imp.g:96:100: ( class_ref )?
                    if stream_class_ref.hasNext():
                        self._adaptor.addChild(root_1, stream_class_ref.nextTree())


                    stream_class_ref.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "implementation_def"


    class implement_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "implement_def"
    # Imp.g:100:1: implement_def : 'implement' class_ref 'using' ns_ref ( ',' ns_ref )* ( 'when' expression )? -> ^( DEF_IMPLEMENT class_ref ^( LIST ( ns_ref )+ ) ( expression )? ) ;
    def implement_def(self, ):
        retval = self.implement_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal57 = None
        string_literal59 = None
        char_literal61 = None
        string_literal63 = None
        class_ref58 = None
        ns_ref60 = None
        ns_ref62 = None
        expression64 = None

        string_literal57_tree = None
        string_literal59_tree = None
        char_literal61_tree = None
        string_literal63_tree = None
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_86 = RewriteRuleTokenStream(self._adaptor, "token 86")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:101:2: ( 'implement' class_ref 'using' ns_ref ( ',' ns_ref )* ( 'when' expression )? -> ^( DEF_IMPLEMENT class_ref ^( LIST ( ns_ref )+ ) ( expression )? ) )
                # Imp.g:101:4: 'implement' class_ref 'using' ns_ref ( ',' ns_ref )* ( 'when' expression )?
                pass 
                string_literal57 = self.match(self.input, 74, self.FOLLOW_74_in_implement_def615) 
                if self._state.backtracking == 0:
                    stream_74.add(string_literal57)


                self._state.following.append(self.FOLLOW_class_ref_in_implement_def617)
                class_ref58 = self.class_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_class_ref.add(class_ref58.tree)


                string_literal59 = self.match(self.input, 86, self.FOLLOW_86_in_implement_def619) 
                if self._state.backtracking == 0:
                    stream_86.add(string_literal59)


                self._state.following.append(self.FOLLOW_ns_ref_in_implement_def621)
                ns_ref60 = self.ns_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_ns_ref.add(ns_ref60.tree)


                # Imp.g:101:41: ( ',' ns_ref )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 53) :
                        alt11 = 1


                    if alt11 == 1:
                        # Imp.g:101:42: ',' ns_ref
                        pass 
                        char_literal61 = self.match(self.input, 53, self.FOLLOW_53_in_implement_def624) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal61)


                        self._state.following.append(self.FOLLOW_ns_ref_in_implement_def626)
                        ns_ref62 = self.ns_ref()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ns_ref.add(ns_ref62.tree)



                    else:
                        break #loop11


                # Imp.g:101:55: ( 'when' expression )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 87) :
                    alt12 = 1
                if alt12 == 1:
                    # Imp.g:101:56: 'when' expression
                    pass 
                    string_literal63 = self.match(self.input, 87, self.FOLLOW_87_in_implement_def631) 
                    if self._state.backtracking == 0:
                        stream_87.add(string_literal63)


                    self._state.following.append(self.FOLLOW_expression_in_implement_def633)
                    expression64 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression64.tree)





                # AST Rewrite
                # elements: expression, class_ref, ns_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 101:76: -> ^( DEF_IMPLEMENT class_ref ^( LIST ( ns_ref )+ ) ( expression )? )
                    # Imp.g:101:79: ^( DEF_IMPLEMENT class_ref ^( LIST ( ns_ref )+ ) ( expression )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DEF_IMPLEMENT, "DEF_IMPLEMENT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_class_ref.nextTree())

                    # Imp.g:101:105: ^( LIST ( ns_ref )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    # Imp.g:101:112: ( ns_ref )+
                    if not (stream_ns_ref.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ns_ref.hasNext():
                        self._adaptor.addChild(root_2, stream_ns_ref.nextTree())


                    stream_ns_ref.reset()

                    self._adaptor.addChild(root_1, root_2)

                    # Imp.g:101:121: ( expression )?
                    if stream_expression.hasNext():
                        self._adaptor.addChild(root_1, stream_expression.nextTree())


                    stream_expression.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "implement_def"


    class implementation_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "implementation"
    # Imp.g:104:1: implementation : ':' ( ML_STRING )? ( statement )* 'end' -> ^( LIST ( statement )* ) ;
    def implementation(self, ):
        retval = self.implementation_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal65 = None
        ML_STRING66 = None
        string_literal68 = None
        statement67 = None

        char_literal65_tree = None
        ML_STRING66_tree = None
        string_literal68_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_ML_STRING = RewriteRuleTokenStream(self._adaptor, "token ML_STRING")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # Imp.g:105:2: ( ':' ( ML_STRING )? ( statement )* 'end' -> ^( LIST ( statement )* ) )
                # Imp.g:105:4: ':' ( ML_STRING )? ( statement )* 'end'
                pass 
                char_literal65 = self.match(self.input, 57, self.FOLLOW_57_in_implementation665) 
                if self._state.backtracking == 0:
                    stream_57.add(char_literal65)


                # Imp.g:105:8: ( ML_STRING )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == ML_STRING) :
                    alt13 = 1
                if alt13 == 1:
                    # Imp.g:105:8: ML_STRING
                    pass 
                    ML_STRING66 = self.match(self.input, ML_STRING, self.FOLLOW_ML_STRING_in_implementation667) 
                    if self._state.backtracking == 0:
                        stream_ML_STRING.add(ML_STRING66)





                # Imp.g:105:19: ( statement )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == CLASS_ID or LA14_0 == ENUM_KEY or LA14_0 == ID or LA14_0 == 73 or LA14_0 == 77) :
                        alt14 = 1


                    if alt14 == 1:
                        # Imp.g:105:19: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_implementation670)
                        statement67 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement67.tree)



                    else:
                        break #loop14


                string_literal68 = self.match(self.input, 70, self.FOLLOW_70_in_implementation673) 
                if self._state.backtracking == 0:
                    stream_70.add(string_literal68)


                # AST Rewrite
                # elements: statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 105:36: -> ^( LIST ( statement )* )
                    # Imp.g:105:39: ^( LIST ( statement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # Imp.g:105:46: ( statement )*
                    while stream_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_statement.nextTree())


                    stream_statement.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "implementation"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "statement"
    # Imp.g:108:1: statement : top_statement -> ^( STATEMENT top_statement ) ;
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        top_statement69 = None

        stream_top_statement = RewriteRuleSubtreeStream(self._adaptor, "rule top_statement")
        try:
            try:
                # Imp.g:109:2: ( top_statement -> ^( STATEMENT top_statement ) )
                # Imp.g:109:4: top_statement
                pass 
                self._state.following.append(self.FOLLOW_top_statement_in_statement693)
                top_statement69 = self.top_statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_top_statement.add(top_statement69.tree)


                # AST Rewrite
                # elements: top_statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 109:18: -> ^( STATEMENT top_statement )
                    # Imp.g:109:21: ^( STATEMENT top_statement )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(STATEMENT, "STATEMENT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_top_statement.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "statement"


    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "parameter"
    # Imp.g:112:1: parameter : ID '=' operand -> ^( ASSIGN ID operand ) ;
    def parameter(self, ):
        retval = self.parameter_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID70 = None
        char_literal71 = None
        operand72 = None

        ID70_tree = None
        char_literal71_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_operand = RewriteRuleSubtreeStream(self._adaptor, "rule operand")
        try:
            try:
                # Imp.g:113:2: ( ID '=' operand -> ^( ASSIGN ID operand ) )
                # Imp.g:113:4: ID '=' operand
                pass 
                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_parameter713) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID70)


                char_literal71 = self.match(self.input, 62, self.FOLLOW_62_in_parameter715) 
                if self._state.backtracking == 0:
                    stream_62.add(char_literal71)


                self._state.following.append(self.FOLLOW_operand_in_parameter717)
                operand72 = self.operand()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_operand.add(operand72.tree)


                # AST Rewrite
                # elements: operand, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 113:19: -> ^( ASSIGN ID operand )
                    # Imp.g:113:22: ^( ASSIGN ID operand )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ASSIGN, "ASSIGN")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_operand.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "parameter"


    class constructor_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "constructor"
    # Imp.g:116:1: constructor : class_ref '(' ( param_list )? ')' -> ^( CONSTRUCT class_ref ( param_list )? ) ;
    def constructor(self, ):
        retval = self.constructor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal74 = None
        char_literal76 = None
        class_ref73 = None
        param_list75 = None

        char_literal74_tree = None
        char_literal76_tree = None
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        stream_param_list = RewriteRuleSubtreeStream(self._adaptor, "rule param_list")
        try:
            try:
                # Imp.g:117:2: ( class_ref '(' ( param_list )? ')' -> ^( CONSTRUCT class_ref ( param_list )? ) )
                # Imp.g:117:4: class_ref '(' ( param_list )? ')'
                pass 
                self._state.following.append(self.FOLLOW_class_ref_in_constructor738)
                class_ref73 = self.class_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_class_ref.add(class_ref73.tree)


                char_literal74 = self.match(self.input, 51, self.FOLLOW_51_in_constructor740) 
                if self._state.backtracking == 0:
                    stream_51.add(char_literal74)


                # Imp.g:117:18: ( param_list )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == ID) :
                    alt15 = 1
                if alt15 == 1:
                    # Imp.g:117:18: param_list
                    pass 
                    self._state.following.append(self.FOLLOW_param_list_in_constructor742)
                    param_list75 = self.param_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_param_list.add(param_list75.tree)





                char_literal76 = self.match(self.input, 52, self.FOLLOW_52_in_constructor745) 
                if self._state.backtracking == 0:
                    stream_52.add(char_literal76)


                # AST Rewrite
                # elements: param_list, class_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 117:34: -> ^( CONSTRUCT class_ref ( param_list )? )
                    # Imp.g:117:37: ^( CONSTRUCT class_ref ( param_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(CONSTRUCT, "CONSTRUCT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_class_ref.nextTree())

                    # Imp.g:117:59: ( param_list )?
                    if stream_param_list.hasNext():
                        self._adaptor.addChild(root_1, stream_param_list.nextTree())


                    stream_param_list.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "constructor"


    class param_list_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "param_list"
    # Imp.g:120:1: param_list : parameter ( ',' parameter )* ( ',' )? -> ^( LIST ( parameter )+ ) ;
    def param_list(self, ):
        retval = self.param_list_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal78 = None
        char_literal80 = None
        parameter77 = None
        parameter79 = None

        char_literal78_tree = None
        char_literal80_tree = None
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # Imp.g:121:2: ( parameter ( ',' parameter )* ( ',' )? -> ^( LIST ( parameter )+ ) )
                # Imp.g:121:4: parameter ( ',' parameter )* ( ',' )?
                pass 
                self._state.following.append(self.FOLLOW_parameter_in_param_list770)
                parameter77 = self.parameter()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_parameter.add(parameter77.tree)


                # Imp.g:121:14: ( ',' parameter )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 53) :
                        LA16_1 = self.input.LA(2)

                        if (LA16_1 == ID) :
                            alt16 = 1




                    if alt16 == 1:
                        # Imp.g:121:15: ',' parameter
                        pass 
                        char_literal78 = self.match(self.input, 53, self.FOLLOW_53_in_param_list773) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal78)


                        self._state.following.append(self.FOLLOW_parameter_in_param_list775)
                        parameter79 = self.parameter()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameter.add(parameter79.tree)



                    else:
                        break #loop16


                # Imp.g:121:31: ( ',' )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 53) :
                    alt17 = 1
                if alt17 == 1:
                    # Imp.g:121:31: ','
                    pass 
                    char_literal80 = self.match(self.input, 53, self.FOLLOW_53_in_param_list779) 
                    if self._state.backtracking == 0:
                        stream_53.add(char_literal80)





                # AST Rewrite
                # elements: parameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 121:36: -> ^( LIST ( parameter )+ )
                    # Imp.g:121:39: ^( LIST ( parameter )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # Imp.g:121:46: ( parameter )+
                    if not (stream_parameter.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "param_list"


    class typedef_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "typedef"
    # Imp.g:124:1: typedef : ( 'typedef' ID 'as' ns_ref 'matching' ( REGEX | expression ) -> ^( DEF_TYPE ID ns_ref ( expression )? ( REGEX )? ) | 'typedef' CLASS_ID 'as' constructor -> ^( DEF_DEFAULT CLASS_ID constructor ) );
    def typedef(self, ):
        retval = self.typedef_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal81 = None
        ID82 = None
        string_literal83 = None
        string_literal85 = None
        REGEX86 = None
        string_literal88 = None
        CLASS_ID89 = None
        string_literal90 = None
        ns_ref84 = None
        expression87 = None
        constructor91 = None

        string_literal81_tree = None
        ID82_tree = None
        string_literal83_tree = None
        string_literal85_tree = None
        REGEX86_tree = None
        string_literal88_tree = None
        CLASS_ID89_tree = None
        string_literal90_tree = None
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_REGEX = RewriteRuleTokenStream(self._adaptor, "token REGEX")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_80 = RewriteRuleTokenStream(self._adaptor, "token 80")
        stream_CLASS_ID = RewriteRuleTokenStream(self._adaptor, "token CLASS_ID")
        stream_85 = RewriteRuleTokenStream(self._adaptor, "token 85")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_constructor = RewriteRuleSubtreeStream(self._adaptor, "rule constructor")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:125:2: ( 'typedef' ID 'as' ns_ref 'matching' ( REGEX | expression ) -> ^( DEF_TYPE ID ns_ref ( expression )? ( REGEX )? ) | 'typedef' CLASS_ID 'as' constructor -> ^( DEF_DEFAULT CLASS_ID constructor ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == 85) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == ID) :
                        alt19 = 1
                    elif (LA19_1 == CLASS_ID) :
                        alt19 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # Imp.g:125:4: 'typedef' ID 'as' ns_ref 'matching' ( REGEX | expression )
                    pass 
                    string_literal81 = self.match(self.input, 85, self.FOLLOW_85_in_typedef800) 
                    if self._state.backtracking == 0:
                        stream_85.add(string_literal81)


                    ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_typedef802) 
                    if self._state.backtracking == 0:
                        stream_ID.add(ID82)


                    string_literal83 = self.match(self.input, 69, self.FOLLOW_69_in_typedef804) 
                    if self._state.backtracking == 0:
                        stream_69.add(string_literal83)


                    self._state.following.append(self.FOLLOW_ns_ref_in_typedef806)
                    ns_ref84 = self.ns_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_ns_ref.add(ns_ref84.tree)


                    string_literal85 = self.match(self.input, 80, self.FOLLOW_80_in_typedef808) 
                    if self._state.backtracking == 0:
                        stream_80.add(string_literal85)


                    # Imp.g:125:40: ( REGEX | expression )
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == REGEX) :
                        LA18_1 = self.input.LA(2)

                        if (LA18_1 == EOF or LA18_1 == CLASS_ID or LA18_1 == ENUM_KEY or LA18_1 == ID or LA18_1 == ML_STRING or LA18_1 == 71 or (73 <= LA18_1 <= 75) or (77 <= LA18_1 <= 78) or LA18_1 == 85) :
                            alt18 = 1
                        elif (LA18_1 == 50 or LA18_1 == 59 or LA18_1 == 61 or (63 <= LA18_1 <= 65) or LA18_1 == 76 or LA18_1 == 79) :
                            alt18 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 18, 1, self.input)

                            raise nvae


                    elif (LA18_0 == CLASS_ID or (FALSE <= LA18_0 <= FLOAT) or LA18_0 == ID or LA18_0 == INT or LA18_0 == ML_STRING or (STRING <= LA18_0 <= TRUE) or LA18_0 == 51) :
                        alt18 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 18, 0, self.input)

                        raise nvae


                    if alt18 == 1:
                        # Imp.g:125:41: REGEX
                        pass 
                        REGEX86 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_typedef811) 
                        if self._state.backtracking == 0:
                            stream_REGEX.add(REGEX86)



                    elif alt18 == 2:
                        # Imp.g:125:49: expression
                        pass 
                        self._state.following.append(self.FOLLOW_expression_in_typedef815)
                        expression87 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression87.tree)





                    # AST Rewrite
                    # elements: expression, ns_ref, REGEX, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 125:61: -> ^( DEF_TYPE ID ns_ref ( expression )? ( REGEX )? )
                        # Imp.g:125:64: ^( DEF_TYPE ID ns_ref ( expression )? ( REGEX )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(DEF_TYPE, "DEF_TYPE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_ns_ref.nextTree())

                        # Imp.g:125:85: ( expression )?
                        if stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset();

                        # Imp.g:125:97: ( REGEX )?
                        if stream_REGEX.hasNext():
                            self._adaptor.addChild(root_1, 
                            stream_REGEX.nextNode()
                            )


                        stream_REGEX.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt19 == 2:
                    # Imp.g:126:4: 'typedef' CLASS_ID 'as' constructor
                    pass 
                    string_literal88 = self.match(self.input, 85, self.FOLLOW_85_in_typedef837) 
                    if self._state.backtracking == 0:
                        stream_85.add(string_literal88)


                    CLASS_ID89 = self.match(self.input, CLASS_ID, self.FOLLOW_CLASS_ID_in_typedef839) 
                    if self._state.backtracking == 0:
                        stream_CLASS_ID.add(CLASS_ID89)


                    string_literal90 = self.match(self.input, 69, self.FOLLOW_69_in_typedef841) 
                    if self._state.backtracking == 0:
                        stream_69.add(string_literal90)


                    self._state.following.append(self.FOLLOW_constructor_in_typedef843)
                    constructor91 = self.constructor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_constructor.add(constructor91.tree)


                    # AST Rewrite
                    # elements: constructor, CLASS_ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 126:40: -> ^( DEF_DEFAULT CLASS_ID constructor )
                        # Imp.g:126:43: ^( DEF_DEFAULT CLASS_ID constructor )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(DEF_DEFAULT, "DEF_DEFAULT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_CLASS_ID.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_constructor.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "typedef"


    class multiplicity_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "multiplicity_body"
    # Imp.g:129:1: multiplicity_body : ( ( INT )=> INT -> ^( MULT INT ) | ( INT ':' )=> INT ':' -> ^( MULT INT NONE ) | ( INT ':' INT )=> INT ':' INT -> ^( MULT INT INT ) | ( ':' INT )=> ':' INT -> ^( MULT NONE INT ) );
    def multiplicity_body(self, ):
        retval = self.multiplicity_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT92 = None
        INT93 = None
        char_literal94 = None
        INT95 = None
        char_literal96 = None
        INT97 = None
        char_literal98 = None
        INT99 = None

        INT92_tree = None
        INT93_tree = None
        char_literal94_tree = None
        INT95_tree = None
        char_literal96_tree = None
        INT97_tree = None
        char_literal98_tree = None
        INT99_tree = None
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")

        try:
            try:
                # Imp.g:130:2: ( ( INT )=> INT -> ^( MULT INT ) | ( INT ':' )=> INT ':' -> ^( MULT INT NONE ) | ( INT ':' INT )=> INT ':' INT -> ^( MULT INT INT ) | ( ':' INT )=> ':' INT -> ^( MULT NONE INT ) )
                alt20 = 4
                LA20_0 = self.input.LA(1)

                if (LA20_0 == INT) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 57) :
                        LA20_3 = self.input.LA(3)

                        if (LA20_3 == INT) and (self.synpred6_Imp()):
                            alt20 = 3
                        elif (LA20_3 == 67) and (self.synpred5_Imp()):
                            alt20 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 20, 3, self.input)

                            raise nvae


                    elif (LA20_1 == 67) and (self.synpred4_Imp()):
                        alt20 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                elif (LA20_0 == 57) and (self.synpred7_Imp()):
                    alt20 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # Imp.g:130:4: ( INT )=> INT
                    pass 
                    INT92 = self.match(self.input, INT, self.FOLLOW_INT_in_multiplicity_body871) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT92)


                    # AST Rewrite
                    # elements: INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 130:17: -> ^( MULT INT )
                        # Imp.g:130:20: ^( MULT INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MULT, "MULT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_INT.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 2:
                    # Imp.g:131:4: ( INT ':' )=> INT ':'
                    pass 
                    INT93 = self.match(self.input, INT, self.FOLLOW_INT_in_multiplicity_body892) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT93)


                    char_literal94 = self.match(self.input, 57, self.FOLLOW_57_in_multiplicity_body894) 
                    if self._state.backtracking == 0:
                        stream_57.add(char_literal94)


                    # AST Rewrite
                    # elements: INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 131:25: -> ^( MULT INT NONE )
                        # Imp.g:131:28: ^( MULT INT NONE )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MULT, "MULT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_INT.nextNode()
                        )

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(NONE, "NONE")
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 3:
                    # Imp.g:132:4: ( INT ':' INT )=> INT ':' INT
                    pass 
                    INT95 = self.match(self.input, INT, self.FOLLOW_INT_in_multiplicity_body919) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT95)


                    char_literal96 = self.match(self.input, 57, self.FOLLOW_57_in_multiplicity_body921) 
                    if self._state.backtracking == 0:
                        stream_57.add(char_literal96)


                    INT97 = self.match(self.input, INT, self.FOLLOW_INT_in_multiplicity_body923) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT97)


                    # AST Rewrite
                    # elements: INT, INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 132:33: -> ^( MULT INT INT )
                        # Imp.g:132:36: ^( MULT INT INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MULT, "MULT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_INT.nextNode()
                        )

                        self._adaptor.addChild(root_1, 
                        stream_INT.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 4:
                    # Imp.g:133:4: ( ':' INT )=> ':' INT
                    pass 
                    char_literal98 = self.match(self.input, 57, self.FOLLOW_57_in_multiplicity_body946) 
                    if self._state.backtracking == 0:
                        stream_57.add(char_literal98)


                    INT99 = self.match(self.input, INT, self.FOLLOW_INT_in_multiplicity_body948) 
                    if self._state.backtracking == 0:
                        stream_INT.add(INT99)


                    # AST Rewrite
                    # elements: INT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 133:25: -> ^( MULT NONE INT )
                        # Imp.g:133:28: ^( MULT NONE INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MULT, "MULT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(NONE, "NONE")
                        )

                        self._adaptor.addChild(root_1, 
                        stream_INT.nextNode()
                        )

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "multiplicity_body"


    class multiplicity_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "multiplicity"
    # Imp.g:137:1: multiplicity : '[' multiplicity_body ']' -> multiplicity_body ;
    def multiplicity(self, ):
        retval = self.multiplicity_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal100 = None
        char_literal102 = None
        multiplicity_body101 = None

        char_literal100_tree = None
        char_literal102_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_multiplicity_body = RewriteRuleSubtreeStream(self._adaptor, "rule multiplicity_body")
        try:
            try:
                # Imp.g:138:2: ( '[' multiplicity_body ']' -> multiplicity_body )
                # Imp.g:138:4: '[' multiplicity_body ']'
                pass 
                char_literal100 = self.match(self.input, 66, self.FOLLOW_66_in_multiplicity970) 
                if self._state.backtracking == 0:
                    stream_66.add(char_literal100)


                self._state.following.append(self.FOLLOW_multiplicity_body_in_multiplicity972)
                multiplicity_body101 = self.multiplicity_body()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_multiplicity_body.add(multiplicity_body101.tree)


                char_literal102 = self.match(self.input, 67, self.FOLLOW_67_in_multiplicity974) 
                if self._state.backtracking == 0:
                    stream_67.add(char_literal102)


                # AST Rewrite
                # elements: multiplicity_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 138:30: -> multiplicity_body
                    self._adaptor.addChild(root_0, stream_multiplicity_body.nextTree())




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "multiplicity"


    class relation_end_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relation_end"
    # Imp.g:141:1: relation_end : class_ref ID -> class_ref ID ;
    def relation_end(self, ):
        retval = self.relation_end_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID104 = None
        class_ref103 = None

        ID104_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        try:
            try:
                # Imp.g:142:2: ( class_ref ID -> class_ref ID )
                # Imp.g:142:4: class_ref ID
                pass 
                self._state.following.append(self.FOLLOW_class_ref_in_relation_end989)
                class_ref103 = self.class_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_class_ref.add(class_ref103.tree)


                ID104 = self.match(self.input, ID, self.FOLLOW_ID_in_relation_end991) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID104)


                # AST Rewrite
                # elements: ID, class_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 142:17: -> class_ref ID
                    self._adaptor.addChild(root_0, stream_class_ref.nextTree())

                    self._adaptor.addChild(root_0, 
                    stream_ID.nextNode()
                    )




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "relation_end"


    class relation_link_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relation_link"
    # Imp.g:145:1: relation_link : ( '<-' | '->' | '--' );
    def relation_link(self, ):
        retval = self.relation_link_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set105 = None

        set105_tree = None

        try:
            try:
                # Imp.g:146:2: ( '<-' | '->' | '--' )
                # Imp.g:
                pass 
                root_0 = self._adaptor.nil()


                set105 = self.input.LT(1)

                if (54 <= self.input.LA(1) <= 55) or self.input.LA(1) == 60:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set105))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "relation_link"


    class relation_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relation"
    # Imp.g:149:1: relation : (left_end= relation_end left_m= multiplicity ) relation_link (right_m= multiplicity right_end= relation_end ) -> ^( DEF_RELATION relation_link ^( LIST $left_end $left_m) ^( LIST $right_end $right_m) ) ;
    def relation(self, ):
        retval = self.relation_return()
        retval.start = self.input.LT(1)


        root_0 = None

        left_end = None
        left_m = None
        right_m = None
        right_end = None
        relation_link106 = None

        stream_multiplicity = RewriteRuleSubtreeStream(self._adaptor, "rule multiplicity")
        stream_relation_link = RewriteRuleSubtreeStream(self._adaptor, "rule relation_link")
        stream_relation_end = RewriteRuleSubtreeStream(self._adaptor, "rule relation_end")
        try:
            try:
                # Imp.g:150:2: ( (left_end= relation_end left_m= multiplicity ) relation_link (right_m= multiplicity right_end= relation_end ) -> ^( DEF_RELATION relation_link ^( LIST $left_end $left_m) ^( LIST $right_end $right_m) ) )
                # Imp.g:150:4: (left_end= relation_end left_m= multiplicity ) relation_link (right_m= multiplicity right_end= relation_end )
                pass 
                # Imp.g:150:4: (left_end= relation_end left_m= multiplicity )
                # Imp.g:150:5: left_end= relation_end left_m= multiplicity
                pass 
                self._state.following.append(self.FOLLOW_relation_end_in_relation1032)
                left_end = self.relation_end()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_relation_end.add(left_end.tree)


                self._state.following.append(self.FOLLOW_multiplicity_in_relation1036)
                left_m = self.multiplicity()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_multiplicity.add(left_m.tree)





                self._state.following.append(self.FOLLOW_relation_link_in_relation1039)
                relation_link106 = self.relation_link()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_relation_link.add(relation_link106.tree)


                # Imp.g:150:62: (right_m= multiplicity right_end= relation_end )
                # Imp.g:150:63: right_m= multiplicity right_end= relation_end
                pass 
                self._state.following.append(self.FOLLOW_multiplicity_in_relation1044)
                right_m = self.multiplicity()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_multiplicity.add(right_m.tree)


                self._state.following.append(self.FOLLOW_relation_end_in_relation1048)
                right_end = self.relation_end()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_relation_end.add(right_end.tree)





                # AST Rewrite
                # elements: left_m, right_end, right_m, relation_link, left_end
                # token labels: 
                # rule labels: retval, right_end, left_m, right_m, left_end
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    if right_end is not None:
                        stream_right_end = RewriteRuleSubtreeStream(self._adaptor, "rule right_end", right_end.tree)
                    else:
                        stream_right_end = RewriteRuleSubtreeStream(self._adaptor, "token right_end", None)

                    if left_m is not None:
                        stream_left_m = RewriteRuleSubtreeStream(self._adaptor, "rule left_m", left_m.tree)
                    else:
                        stream_left_m = RewriteRuleSubtreeStream(self._adaptor, "token left_m", None)

                    if right_m is not None:
                        stream_right_m = RewriteRuleSubtreeStream(self._adaptor, "rule right_m", right_m.tree)
                    else:
                        stream_right_m = RewriteRuleSubtreeStream(self._adaptor, "token right_m", None)

                    if left_end is not None:
                        stream_left_end = RewriteRuleSubtreeStream(self._adaptor, "rule left_end", left_end.tree)
                    else:
                        stream_left_end = RewriteRuleSubtreeStream(self._adaptor, "token left_end", None)


                    root_0 = self._adaptor.nil()
                    # 150:108: -> ^( DEF_RELATION relation_link ^( LIST $left_end $left_m) ^( LIST $right_end $right_m) )
                    # Imp.g:151:3: ^( DEF_RELATION relation_link ^( LIST $left_end $left_m) ^( LIST $right_end $right_m) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DEF_RELATION, "DEF_RELATION")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_relation_link.nextTree())

                    # Imp.g:151:32: ^( LIST $left_end $left_m)
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_left_end.nextTree())

                    self._adaptor.addChild(root_2, stream_left_m.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    # Imp.g:151:58: ^( LIST $right_end $right_m)
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_right_end.nextTree())

                    self._adaptor.addChild(root_2, stream_right_m.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "relation"


    class operand_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "operand"
    # Imp.g:154:1: operand : ( constant | list_def | index_lookup | ( ns_ref '(' )=> function_call | class_ref | variable | method_call | ( '{' )=> '{' expression '}' -> ^( EXPRESSION expression ) );
    def operand(self, ):
        retval = self.operand_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal114 = None
        char_literal116 = None
        constant107 = None
        list_def108 = None
        index_lookup109 = None
        function_call110 = None
        class_ref111 = None
        variable112 = None
        method_call113 = None
        expression115 = None

        char_literal114_tree = None
        char_literal116_tree = None
        stream_91 = RewriteRuleTokenStream(self._adaptor, "token 91")
        stream_89 = RewriteRuleTokenStream(self._adaptor, "token 89")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        try:
            try:
                # Imp.g:155:2: ( constant | list_def | index_lookup | ( ns_ref '(' )=> function_call | class_ref | variable | method_call | ( '{' )=> '{' expression '}' -> ^( EXPRESSION expression ) )
                alt21 = 8
                alt21 = self.dfa21.predict(self.input)
                if alt21 == 1:
                    # Imp.g:155:4: constant
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_constant_in_operand1091)
                    constant107 = self.constant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, constant107.tree)



                elif alt21 == 2:
                    # Imp.g:156:4: list_def
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_def_in_operand1096)
                    list_def108 = self.list_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_def108.tree)



                elif alt21 == 3:
                    # Imp.g:157:4: index_lookup
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_index_lookup_in_operand1101)
                    index_lookup109 = self.index_lookup()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, index_lookup109.tree)



                elif alt21 == 4:
                    # Imp.g:158:4: ( ns_ref '(' )=> function_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_function_call_in_operand1114)
                    function_call110 = self.function_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function_call110.tree)



                elif alt21 == 5:
                    # Imp.g:159:4: class_ref
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_class_ref_in_operand1119)
                    class_ref111 = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, class_ref111.tree)



                elif alt21 == 6:
                    # Imp.g:160:4: variable
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_variable_in_operand1124)
                    variable112 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable112.tree)



                elif alt21 == 7:
                    # Imp.g:161:4: method_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_method_call_in_operand1129)
                    method_call113 = self.method_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, method_call113.tree)



                elif alt21 == 8:
                    # Imp.g:162:4: ( '{' )=> '{' expression '}'
                    pass 
                    char_literal114 = self.match(self.input, 89, self.FOLLOW_89_in_operand1140) 
                    if self._state.backtracking == 0:
                        stream_89.add(char_literal114)


                    self._state.following.append(self.FOLLOW_expression_in_operand1142)
                    expression115 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression115.tree)


                    char_literal116 = self.match(self.input, 91, self.FOLLOW_91_in_operand1144) 
                    if self._state.backtracking == 0:
                        stream_91.add(char_literal116)


                    # AST Rewrite
                    # elements: expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 162:32: -> ^( EXPRESSION expression )
                        # Imp.g:162:35: ^( EXPRESSION expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(EXPRESSION, "EXPRESSION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "operand"


    class constant_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "constant"
    # Imp.g:166:1: constant : ( TRUE | FALSE | STRING | INT | FLOAT | REGEX | ML_STRING );
    def constant(self, ):
        retval = self.constant_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set117 = None

        set117_tree = None

        try:
            try:
                # Imp.g:167:2: ( TRUE | FALSE | STRING | INT | FLOAT | REGEX | ML_STRING )
                # Imp.g:
                pass 
                root_0 = self._adaptor.nil()


                set117 = self.input.LT(1)

                if (FALSE <= self.input.LA(1) <= FLOAT) or self.input.LA(1) == INT or self.input.LA(1) == ML_STRING or self.input.LA(1) == REGEX or (STRING <= self.input.LA(1) <= TRUE):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set117))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "constant"


    class list_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "list_def"
    # Imp.g:170:1: list_def : '[' operand ( ',' operand )* ( ',' )? ']' -> ^( LIST ( operand )+ ) ;
    def list_def(self, ):
        retval = self.list_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal118 = None
        char_literal120 = None
        char_literal122 = None
        char_literal123 = None
        operand119 = None
        operand121 = None

        char_literal118_tree = None
        char_literal120_tree = None
        char_literal122_tree = None
        char_literal123_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_operand = RewriteRuleSubtreeStream(self._adaptor, "rule operand")
        try:
            try:
                # Imp.g:171:2: ( '[' operand ( ',' operand )* ( ',' )? ']' -> ^( LIST ( operand )+ ) )
                # Imp.g:171:4: '[' operand ( ',' operand )* ( ',' )? ']'
                pass 
                char_literal118 = self.match(self.input, 66, self.FOLLOW_66_in_list_def1210) 
                if self._state.backtracking == 0:
                    stream_66.add(char_literal118)


                self._state.following.append(self.FOLLOW_operand_in_list_def1212)
                operand119 = self.operand()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_operand.add(operand119.tree)


                # Imp.g:171:16: ( ',' operand )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == 53) :
                        LA22_1 = self.input.LA(2)

                        if (LA22_1 == CLASS_ID or (FALSE <= LA22_1 <= FLOAT) or LA22_1 == ID or LA22_1 == INT or LA22_1 == ML_STRING or LA22_1 == REGEX or (STRING <= LA22_1 <= TRUE) or LA22_1 == 66 or LA22_1 == 89) :
                            alt22 = 1




                    if alt22 == 1:
                        # Imp.g:171:17: ',' operand
                        pass 
                        char_literal120 = self.match(self.input, 53, self.FOLLOW_53_in_list_def1215) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal120)


                        self._state.following.append(self.FOLLOW_operand_in_list_def1217)
                        operand121 = self.operand()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_operand.add(operand121.tree)



                    else:
                        break #loop22


                # Imp.g:171:31: ( ',' )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 53) :
                    alt23 = 1
                if alt23 == 1:
                    # Imp.g:171:31: ','
                    pass 
                    char_literal122 = self.match(self.input, 53, self.FOLLOW_53_in_list_def1221) 
                    if self._state.backtracking == 0:
                        stream_53.add(char_literal122)





                char_literal123 = self.match(self.input, 67, self.FOLLOW_67_in_list_def1224) 
                if self._state.backtracking == 0:
                    stream_67.add(char_literal123)


                # AST Rewrite
                # elements: operand
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 171:40: -> ^( LIST ( operand )+ )
                    # Imp.g:171:43: ^( LIST ( operand )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # Imp.g:171:50: ( operand )+
                    if not (stream_operand.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_operand.hasNext():
                        self._adaptor.addChild(root_1, stream_operand.nextTree())


                    stream_operand.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "list_def"


    class index_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "index_arg"
    # Imp.g:174:1: index_arg : param_list ;
    def index_arg(self, ):
        retval = self.index_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        param_list124 = None


        try:
            try:
                # Imp.g:175:2: ( param_list )
                # Imp.g:175:4: param_list
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_param_list_in_index_arg1245)
                param_list124 = self.param_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, param_list124.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "index_arg"


    class index_lookup_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "index_lookup"
    # Imp.g:178:1: index_lookup : class_ref '[' index_arg ']' -> ^( HASH class_ref index_arg ) ;
    def index_lookup(self, ):
        retval = self.index_lookup_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal126 = None
        char_literal128 = None
        class_ref125 = None
        index_arg127 = None

        char_literal126_tree = None
        char_literal128_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        stream_index_arg = RewriteRuleSubtreeStream(self._adaptor, "rule index_arg")
        try:
            try:
                # Imp.g:180:2: ( class_ref '[' index_arg ']' -> ^( HASH class_ref index_arg ) )
                # Imp.g:180:4: class_ref '[' index_arg ']'
                pass 
                self._state.following.append(self.FOLLOW_class_ref_in_index_lookup1258)
                class_ref125 = self.class_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_class_ref.add(class_ref125.tree)


                char_literal126 = self.match(self.input, 66, self.FOLLOW_66_in_index_lookup1260) 
                if self._state.backtracking == 0:
                    stream_66.add(char_literal126)


                self._state.following.append(self.FOLLOW_index_arg_in_index_lookup1262)
                index_arg127 = self.index_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_index_arg.add(index_arg127.tree)


                char_literal128 = self.match(self.input, 67, self.FOLLOW_67_in_index_lookup1264) 
                if self._state.backtracking == 0:
                    stream_67.add(char_literal128)


                # AST Rewrite
                # elements: index_arg, class_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 180:32: -> ^( HASH class_ref index_arg )
                    # Imp.g:180:35: ^( HASH class_ref index_arg )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(HASH, "HASH")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_class_ref.nextTree())

                    self._adaptor.addChild(root_1, stream_index_arg.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "index_lookup"


    class entity_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "entity_def"
    # Imp.g:183:1: entity_def : ( 'entity' CLASS_ID ( 'extends' class_ref ( ',' class_ref )* )? ) ':' ( ML_STRING )? ( entity_body )* 'end' -> ^( DEF_ENTITY CLASS_ID ^( LIST ( class_ref )* ) ^( LIST ( entity_body )* ) ( ML_STRING )? ) ;
    def entity_def(self, ):
        retval = self.entity_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal129 = None
        CLASS_ID130 = None
        string_literal131 = None
        char_literal133 = None
        char_literal135 = None
        ML_STRING136 = None
        string_literal138 = None
        class_ref132 = None
        class_ref134 = None
        entity_body137 = None

        string_literal129_tree = None
        CLASS_ID130_tree = None
        string_literal131_tree = None
        char_literal133_tree = None
        char_literal135_tree = None
        ML_STRING136_tree = None
        string_literal138_tree = None
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_ML_STRING = RewriteRuleTokenStream(self._adaptor, "token ML_STRING")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_CLASS_ID = RewriteRuleTokenStream(self._adaptor, "token CLASS_ID")
        stream_entity_body = RewriteRuleSubtreeStream(self._adaptor, "rule entity_body")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        try:
            try:
                # Imp.g:184:2: ( ( 'entity' CLASS_ID ( 'extends' class_ref ( ',' class_ref )* )? ) ':' ( ML_STRING )? ( entity_body )* 'end' -> ^( DEF_ENTITY CLASS_ID ^( LIST ( class_ref )* ) ^( LIST ( entity_body )* ) ( ML_STRING )? ) )
                # Imp.g:184:4: ( 'entity' CLASS_ID ( 'extends' class_ref ( ',' class_ref )* )? ) ':' ( ML_STRING )? ( entity_body )* 'end'
                pass 
                # Imp.g:184:4: ( 'entity' CLASS_ID ( 'extends' class_ref ( ',' class_ref )* )? )
                # Imp.g:184:5: 'entity' CLASS_ID ( 'extends' class_ref ( ',' class_ref )* )?
                pass 
                string_literal129 = self.match(self.input, 71, self.FOLLOW_71_in_entity_def1286) 
                if self._state.backtracking == 0:
                    stream_71.add(string_literal129)


                CLASS_ID130 = self.match(self.input, CLASS_ID, self.FOLLOW_CLASS_ID_in_entity_def1288) 
                if self._state.backtracking == 0:
                    stream_CLASS_ID.add(CLASS_ID130)


                # Imp.g:184:23: ( 'extends' class_ref ( ',' class_ref )* )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == 72) :
                    alt25 = 1
                if alt25 == 1:
                    # Imp.g:184:24: 'extends' class_ref ( ',' class_ref )*
                    pass 
                    string_literal131 = self.match(self.input, 72, self.FOLLOW_72_in_entity_def1291) 
                    if self._state.backtracking == 0:
                        stream_72.add(string_literal131)


                    self._state.following.append(self.FOLLOW_class_ref_in_entity_def1293)
                    class_ref132 = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_ref.add(class_ref132.tree)


                    # Imp.g:184:44: ( ',' class_ref )*
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == 53) :
                            alt24 = 1


                        if alt24 == 1:
                            # Imp.g:184:45: ',' class_ref
                            pass 
                            char_literal133 = self.match(self.input, 53, self.FOLLOW_53_in_entity_def1296) 
                            if self._state.backtracking == 0:
                                stream_53.add(char_literal133)


                            self._state.following.append(self.FOLLOW_class_ref_in_entity_def1298)
                            class_ref134 = self.class_ref()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_class_ref.add(class_ref134.tree)



                        else:
                            break #loop24








                char_literal135 = self.match(self.input, 57, self.FOLLOW_57_in_entity_def1305) 
                if self._state.backtracking == 0:
                    stream_57.add(char_literal135)


                # Imp.g:184:68: ( ML_STRING )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == ML_STRING) :
                    alt26 = 1
                if alt26 == 1:
                    # Imp.g:184:68: ML_STRING
                    pass 
                    ML_STRING136 = self.match(self.input, ML_STRING, self.FOLLOW_ML_STRING_in_entity_def1307) 
                    if self._state.backtracking == 0:
                        stream_ML_STRING.add(ML_STRING136)





                # Imp.g:184:79: ( entity_body )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == CLASS_ID or LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # Imp.g:184:80: entity_body
                        pass 
                        self._state.following.append(self.FOLLOW_entity_body_in_entity_def1311)
                        entity_body137 = self.entity_body()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_entity_body.add(entity_body137.tree)



                    else:
                        break #loop27


                string_literal138 = self.match(self.input, 70, self.FOLLOW_70_in_entity_def1315) 
                if self._state.backtracking == 0:
                    stream_70.add(string_literal138)


                # AST Rewrite
                # elements: ML_STRING, entity_body, class_ref, CLASS_ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 185:3: -> ^( DEF_ENTITY CLASS_ID ^( LIST ( class_ref )* ) ^( LIST ( entity_body )* ) ( ML_STRING )? )
                    # Imp.g:185:6: ^( DEF_ENTITY CLASS_ID ^( LIST ( class_ref )* ) ^( LIST ( entity_body )* ) ( ML_STRING )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DEF_ENTITY, "DEF_ENTITY")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_CLASS_ID.nextNode()
                    )

                    # Imp.g:185:28: ^( LIST ( class_ref )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    # Imp.g:185:35: ( class_ref )*
                    while stream_class_ref.hasNext():
                        self._adaptor.addChild(root_2, stream_class_ref.nextTree())


                    stream_class_ref.reset();

                    self._adaptor.addChild(root_1, root_2)

                    # Imp.g:185:47: ^( LIST ( entity_body )* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_2)

                    # Imp.g:185:54: ( entity_body )*
                    while stream_entity_body.hasNext():
                        self._adaptor.addChild(root_2, stream_entity_body.nextTree())


                    stream_entity_body.reset();

                    self._adaptor.addChild(root_1, root_2)

                    # Imp.g:185:68: ( ML_STRING )?
                    if stream_ML_STRING.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ML_STRING.nextNode()
                        )


                    stream_ML_STRING.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "entity_def"


    class type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "type"
    # Imp.g:188:1: type : ( ns_ref | class_ref );
    def type(self, ):
        retval = self.type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ns_ref139 = None
        class_ref140 = None


        try:
            try:
                # Imp.g:189:2: ( ns_ref | class_ref )
                alt28 = 2
                alt28 = self.dfa28.predict(self.input)
                if alt28 == 1:
                    # Imp.g:189:4: ns_ref
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ns_ref_in_type1357)
                    ns_ref139 = self.ns_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ns_ref139.tree)



                elif alt28 == 2:
                    # Imp.g:189:13: class_ref
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_class_ref_in_type1361)
                    class_ref140 = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, class_ref140.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "type"


    class entity_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "entity_body"
    # Imp.g:192:1: entity_body : type ID ( '=' constant )? -> ^( STATEMENT type ID ( constant )? ) ;
    def entity_body(self, ):
        retval = self.entity_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID142 = None
        char_literal143 = None
        type141 = None
        constant144 = None

        ID142_tree = None
        char_literal143_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_constant = RewriteRuleSubtreeStream(self._adaptor, "rule constant")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # Imp.g:193:2: ( type ID ( '=' constant )? -> ^( STATEMENT type ID ( constant )? ) )
                # Imp.g:193:4: type ID ( '=' constant )?
                pass 
                self._state.following.append(self.FOLLOW_type_in_entity_body1372)
                type141 = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(type141.tree)


                ID142 = self.match(self.input, ID, self.FOLLOW_ID_in_entity_body1374) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID142)


                # Imp.g:193:12: ( '=' constant )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 62) :
                    alt29 = 1
                if alt29 == 1:
                    # Imp.g:193:13: '=' constant
                    pass 
                    char_literal143 = self.match(self.input, 62, self.FOLLOW_62_in_entity_body1377) 
                    if self._state.backtracking == 0:
                        stream_62.add(char_literal143)


                    self._state.following.append(self.FOLLOW_constant_in_entity_body1379)
                    constant144 = self.constant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_constant.add(constant144.tree)





                # AST Rewrite
                # elements: constant, ID, type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 193:28: -> ^( STATEMENT type ID ( constant )? )
                    # Imp.g:193:31: ^( STATEMENT type ID ( constant )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(STATEMENT, "STATEMENT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_type.nextTree())

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # Imp.g:193:51: ( constant )?
                    if stream_constant.hasNext():
                        self._adaptor.addChild(root_1, stream_constant.nextTree())


                    stream_constant.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "entity_body"


    class ns_ref_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "ns_ref"
    # Imp.g:196:1: ns_ref : ID ( '::' ID )* -> ^( REF ( ID )+ ) ;
    def ns_ref(self, ):
        retval = self.ns_ref_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID145 = None
        string_literal146 = None
        ID147 = None

        ID145_tree = None
        string_literal146_tree = None
        ID147_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Imp.g:197:2: ( ID ( '::' ID )* -> ^( REF ( ID )+ ) )
                # Imp.g:197:4: ID ( '::' ID )*
                pass 
                ID145 = self.match(self.input, ID, self.FOLLOW_ID_in_ns_ref1406) 
                if self._state.backtracking == 0:
                    stream_ID.add(ID145)


                # Imp.g:197:7: ( '::' ID )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 58) :
                        alt30 = 1


                    if alt30 == 1:
                        # Imp.g:197:8: '::' ID
                        pass 
                        string_literal146 = self.match(self.input, 58, self.FOLLOW_58_in_ns_ref1409) 
                        if self._state.backtracking == 0:
                            stream_58.add(string_literal146)


                        ID147 = self.match(self.input, ID, self.FOLLOW_ID_in_ns_ref1411) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ID147)



                    else:
                        break #loop30


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 197:18: -> ^( REF ( ID )+ )
                    # Imp.g:197:21: ^( REF ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(REF, "REF")
                    , root_1)

                    # Imp.g:197:27: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "ns_ref"


    class class_ref_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "class_ref"
    # Imp.g:200:1: class_ref : (ns+= ID '::' )* CLASS_ID -> ^( CLASS_REF ^( NS ( $ns)* ) CLASS_ID ) ;
    def class_ref(self, ):
        retval = self.class_ref_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal148 = None
        CLASS_ID149 = None
        ns = None
        list_ns = None

        string_literal148_tree = None
        CLASS_ID149_tree = None
        ns_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CLASS_ID = RewriteRuleTokenStream(self._adaptor, "token CLASS_ID")

        try:
            try:
                # Imp.g:201:5: ( (ns+= ID '::' )* CLASS_ID -> ^( CLASS_REF ^( NS ( $ns)* ) CLASS_ID ) )
                # Imp.g:201:7: (ns+= ID '::' )* CLASS_ID
                pass 
                # Imp.g:201:7: (ns+= ID '::' )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == ID) :
                        alt31 = 1


                    if alt31 == 1:
                        # Imp.g:201:8: ns+= ID '::'
                        pass 
                        ns = self.match(self.input, ID, self.FOLLOW_ID_in_class_ref1440) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ns)

                        if list_ns is None:
                            list_ns = []
                        list_ns.append(ns)


                        string_literal148 = self.match(self.input, 58, self.FOLLOW_58_in_class_ref1442) 
                        if self._state.backtracking == 0:
                            stream_58.add(string_literal148)



                    else:
                        break #loop31


                CLASS_ID149 = self.match(self.input, CLASS_ID, self.FOLLOW_CLASS_ID_in_class_ref1446) 
                if self._state.backtracking == 0:
                    stream_CLASS_ID.add(CLASS_ID149)


                # AST Rewrite
                # elements: CLASS_ID, ns
                # token labels: 
                # rule labels: retval
                # token list labels: ns
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    stream_ns = RewriteRuleTokenStream(self._adaptor, "token ns", list_ns)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 201:31: -> ^( CLASS_REF ^( NS ( $ns)* ) CLASS_ID )
                    # Imp.g:201:34: ^( CLASS_REF ^( NS ( $ns)* ) CLASS_ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(CLASS_REF, "CLASS_REF")
                    , root_1)

                    # Imp.g:201:46: ^( NS ( $ns)* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NS, "NS")
                    , root_2)

                    # Imp.g:201:52: ( $ns)*
                    while stream_ns.hasNext():
                        self._adaptor.addChild(root_2, stream_ns.nextNode())


                    stream_ns.reset();

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_1, 
                    stream_CLASS_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "class_ref"


    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "variable"
    # Imp.g:204:1: variable : (ns+= ID '::' )* var= ID ( '.' attr+= ID )* -> ^( VAR_REF ^( NS ( $ns)* ) $var ^( ATTR ( $attr)* ) ) ;
    def variable(self, ):
        retval = self.variable_return()
        retval.start = self.input.LT(1)


        root_0 = None

        var = None
        string_literal150 = None
        char_literal151 = None
        ns = None
        attr = None
        list_ns = None
        list_attr = None

        var_tree = None
        string_literal150_tree = None
        char_literal151_tree = None
        ns_tree = None
        attr_tree = None
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # Imp.g:205:2: ( (ns+= ID '::' )* var= ID ( '.' attr+= ID )* -> ^( VAR_REF ^( NS ( $ns)* ) $var ^( ATTR ( $attr)* ) ) )
                # Imp.g:205:4: (ns+= ID '::' )* var= ID ( '.' attr+= ID )*
                pass 
                # Imp.g:205:4: (ns+= ID '::' )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ID) :
                        LA32_1 = self.input.LA(2)

                        if (LA32_1 == 58) :
                            alt32 = 1




                    if alt32 == 1:
                        # Imp.g:205:5: ns+= ID '::'
                        pass 
                        ns = self.match(self.input, ID, self.FOLLOW_ID_in_variable1480) 
                        if self._state.backtracking == 0:
                            stream_ID.add(ns)

                        if list_ns is None:
                            list_ns = []
                        list_ns.append(ns)


                        string_literal150 = self.match(self.input, 58, self.FOLLOW_58_in_variable1482) 
                        if self._state.backtracking == 0:
                            stream_58.add(string_literal150)



                    else:
                        break #loop32


                var = self.match(self.input, ID, self.FOLLOW_ID_in_variable1488) 
                if self._state.backtracking == 0:
                    stream_ID.add(var)


                # Imp.g:205:26: ( '.' attr+= ID )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 56) :
                        alt33 = 1


                    if alt33 == 1:
                        # Imp.g:205:27: '.' attr+= ID
                        pass 
                        char_literal151 = self.match(self.input, 56, self.FOLLOW_56_in_variable1491) 
                        if self._state.backtracking == 0:
                            stream_56.add(char_literal151)


                        attr = self.match(self.input, ID, self.FOLLOW_ID_in_variable1495) 
                        if self._state.backtracking == 0:
                            stream_ID.add(attr)

                        if list_attr is None:
                            list_attr = []
                        list_attr.append(attr)



                    else:
                        break #loop33


                # AST Rewrite
                # elements: ns, attr, var
                # token labels: var
                # rule labels: retval
                # token list labels: ns, attr
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    stream_var = RewriteRuleTokenStream(self._adaptor, "token var", var)
                    stream_ns = RewriteRuleTokenStream(self._adaptor, "token ns", list_ns)
                    stream_attr = RewriteRuleTokenStream(self._adaptor, "token attr", list_attr)
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 205:42: -> ^( VAR_REF ^( NS ( $ns)* ) $var ^( ATTR ( $attr)* ) )
                    # Imp.g:205:45: ^( VAR_REF ^( NS ( $ns)* ) $var ^( ATTR ( $attr)* ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(VAR_REF, "VAR_REF")
                    , root_1)

                    # Imp.g:205:55: ^( NS ( $ns)* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NS, "NS")
                    , root_2)

                    # Imp.g:205:61: ( $ns)*
                    while stream_ns.hasNext():
                        self._adaptor.addChild(root_2, stream_ns.nextNode())


                    stream_ns.reset();

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_1, stream_var.nextNode())

                    # Imp.g:205:71: ^( ATTR ( $attr)* )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ATTR, "ATTR")
                    , root_2)

                    # Imp.g:205:79: ( $attr)*
                    while stream_attr.hasNext():
                        self._adaptor.addChild(root_2, stream_attr.nextNode())


                    stream_attr.reset();

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "variable"


    class arg_list_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arg_list"
    # Imp.g:208:1: arg_list : operand ( ',' operand )* ( ',' )? -> ^( LIST ( operand )+ ) ;
    def arg_list(self, ):
        retval = self.arg_list_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal153 = None
        char_literal155 = None
        operand152 = None
        operand154 = None

        char_literal153_tree = None
        char_literal155_tree = None
        stream_53 = RewriteRuleTokenStream(self._adaptor, "token 53")
        stream_operand = RewriteRuleSubtreeStream(self._adaptor, "rule operand")
        try:
            try:
                # Imp.g:209:2: ( operand ( ',' operand )* ( ',' )? -> ^( LIST ( operand )+ ) )
                # Imp.g:209:4: operand ( ',' operand )* ( ',' )?
                pass 
                self._state.following.append(self.FOLLOW_operand_in_arg_list1534)
                operand152 = self.operand()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_operand.add(operand152.tree)


                # Imp.g:209:12: ( ',' operand )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == 53) :
                        LA34_1 = self.input.LA(2)

                        if (LA34_1 == CLASS_ID or (FALSE <= LA34_1 <= FLOAT) or LA34_1 == ID or LA34_1 == INT or LA34_1 == ML_STRING or LA34_1 == REGEX or (STRING <= LA34_1 <= TRUE) or LA34_1 == 66 or LA34_1 == 89) :
                            alt34 = 1




                    if alt34 == 1:
                        # Imp.g:209:13: ',' operand
                        pass 
                        char_literal153 = self.match(self.input, 53, self.FOLLOW_53_in_arg_list1537) 
                        if self._state.backtracking == 0:
                            stream_53.add(char_literal153)


                        self._state.following.append(self.FOLLOW_operand_in_arg_list1539)
                        operand154 = self.operand()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_operand.add(operand154.tree)



                    else:
                        break #loop34


                # Imp.g:209:27: ( ',' )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == 53) :
                    alt35 = 1
                if alt35 == 1:
                    # Imp.g:209:27: ','
                    pass 
                    char_literal155 = self.match(self.input, 53, self.FOLLOW_53_in_arg_list1543) 
                    if self._state.backtracking == 0:
                        stream_53.add(char_literal155)





                # AST Rewrite
                # elements: operand
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 209:32: -> ^( LIST ( operand )+ )
                    # Imp.g:209:35: ^( LIST ( operand )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LIST, "LIST")
                    , root_1)

                    # Imp.g:209:42: ( operand )+
                    if not (stream_operand.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_operand.hasNext():
                        self._adaptor.addChild(root_1, stream_operand.nextTree())


                    stream_operand.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "arg_list"


    class function_call_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "function_call"
    # Imp.g:212:1: function_call : ns_ref '(' ( call_arg )? ')' -> ^( CALL ns_ref ( call_arg )? ) ;
    def function_call(self, ):
        retval = self.function_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal157 = None
        char_literal159 = None
        ns_ref156 = None
        call_arg158 = None

        char_literal157_tree = None
        char_literal159_tree = None
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_call_arg = RewriteRuleSubtreeStream(self._adaptor, "rule call_arg")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:213:2: ( ns_ref '(' ( call_arg )? ')' -> ^( CALL ns_ref ( call_arg )? ) )
                # Imp.g:213:4: ns_ref '(' ( call_arg )? ')'
                pass 
                self._state.following.append(self.FOLLOW_ns_ref_in_function_call1565)
                ns_ref156 = self.ns_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_ns_ref.add(ns_ref156.tree)


                char_literal157 = self.match(self.input, 51, self.FOLLOW_51_in_function_call1567) 
                if self._state.backtracking == 0:
                    stream_51.add(char_literal157)


                # Imp.g:213:15: ( call_arg )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == CLASS_ID or (FALSE <= LA36_0 <= FLOAT) or LA36_0 == ID or LA36_0 == INT or LA36_0 == ML_STRING or LA36_0 == REGEX or (STRING <= LA36_0 <= TRUE) or LA36_0 == 66 or LA36_0 == 89) :
                    alt36 = 1
                if alt36 == 1:
                    # Imp.g:213:15: call_arg
                    pass 
                    self._state.following.append(self.FOLLOW_call_arg_in_function_call1569)
                    call_arg158 = self.call_arg()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_call_arg.add(call_arg158.tree)





                char_literal159 = self.match(self.input, 52, self.FOLLOW_52_in_function_call1572) 
                if self._state.backtracking == 0:
                    stream_52.add(char_literal159)


                # AST Rewrite
                # elements: ns_ref, call_arg
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 213:29: -> ^( CALL ns_ref ( call_arg )? )
                    # Imp.g:213:32: ^( CALL ns_ref ( call_arg )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(CALL, "CALL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_ns_ref.nextTree())

                    # Imp.g:213:46: ( call_arg )?
                    if stream_call_arg.hasNext():
                        self._adaptor.addChild(root_1, stream_call_arg.nextTree())


                    stream_call_arg.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "function_call"


    class call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "call_arg"
    # Imp.g:216:1: call_arg : arg_list ;
    def call_arg(self, ):
        retval = self.call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arg_list160 = None


        try:
            try:
                # Imp.g:217:2: ( arg_list )
                # Imp.g:219:3: arg_list
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_arg_list_in_call_arg1600)
                arg_list160 = self.arg_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arg_list160.tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "call_arg"


    class method_pipe_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "method_pipe"
    # Imp.g:222:1: method_pipe : '|' ns_ref ( '(' ( call_arg )? ')' )? -> ^( CALL ns_ref ( call_arg )? ) ;
    def method_pipe(self, ):
        retval = self.method_pipe_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal161 = None
        char_literal163 = None
        char_literal165 = None
        ns_ref162 = None
        call_arg164 = None

        char_literal161_tree = None
        char_literal163_tree = None
        char_literal165_tree = None
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_90 = RewriteRuleTokenStream(self._adaptor, "token 90")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_call_arg = RewriteRuleSubtreeStream(self._adaptor, "rule call_arg")
        stream_ns_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ns_ref")
        try:
            try:
                # Imp.g:223:2: ( '|' ns_ref ( '(' ( call_arg )? ')' )? -> ^( CALL ns_ref ( call_arg )? ) )
                # Imp.g:223:4: '|' ns_ref ( '(' ( call_arg )? ')' )?
                pass 
                char_literal161 = self.match(self.input, 90, self.FOLLOW_90_in_method_pipe1611) 
                if self._state.backtracking == 0:
                    stream_90.add(char_literal161)


                self._state.following.append(self.FOLLOW_ns_ref_in_method_pipe1613)
                ns_ref162 = self.ns_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_ns_ref.add(ns_ref162.tree)


                # Imp.g:223:15: ( '(' ( call_arg )? ')' )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == 51) :
                    alt38 = 1
                if alt38 == 1:
                    # Imp.g:223:16: '(' ( call_arg )? ')'
                    pass 
                    char_literal163 = self.match(self.input, 51, self.FOLLOW_51_in_method_pipe1616) 
                    if self._state.backtracking == 0:
                        stream_51.add(char_literal163)


                    # Imp.g:223:20: ( call_arg )?
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == CLASS_ID or (FALSE <= LA37_0 <= FLOAT) or LA37_0 == ID or LA37_0 == INT or LA37_0 == ML_STRING or LA37_0 == REGEX or (STRING <= LA37_0 <= TRUE) or LA37_0 == 66 or LA37_0 == 89) :
                        alt37 = 1
                    if alt37 == 1:
                        # Imp.g:223:20: call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_call_arg_in_method_pipe1618)
                        call_arg164 = self.call_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_call_arg.add(call_arg164.tree)





                    char_literal165 = self.match(self.input, 52, self.FOLLOW_52_in_method_pipe1621) 
                    if self._state.backtracking == 0:
                        stream_52.add(char_literal165)





                # AST Rewrite
                # elements: ns_ref, call_arg
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 223:36: -> ^( CALL ns_ref ( call_arg )? )
                    # Imp.g:223:40: ^( CALL ns_ref ( call_arg )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(CALL, "CALL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_ns_ref.nextTree())

                    # Imp.g:223:54: ( call_arg )?
                    if stream_call_arg.hasNext():
                        self._adaptor.addChild(root_1, stream_call_arg.nextTree())


                    stream_call_arg.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "method_pipe"


    class method_call_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "method_call"
    # Imp.g:226:1: method_call : (cl= class_ref |var= variable ) ( method_pipe )+ -> ^( METHOD ( $cl)? ( $var)? ( method_pipe )+ ) ;
    def method_call(self, ):
        retval = self.method_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cl = None
        var = None
        method_pipe166 = None

        stream_method_pipe = RewriteRuleSubtreeStream(self._adaptor, "rule method_pipe")
        stream_class_ref = RewriteRuleSubtreeStream(self._adaptor, "rule class_ref")
        stream_variable = RewriteRuleSubtreeStream(self._adaptor, "rule variable")
        try:
            try:
                # Imp.g:227:2: ( (cl= class_ref |var= variable ) ( method_pipe )+ -> ^( METHOD ( $cl)? ( $var)? ( method_pipe )+ ) )
                # Imp.g:227:4: (cl= class_ref |var= variable ) ( method_pipe )+
                pass 
                # Imp.g:227:4: (cl= class_ref |var= variable )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # Imp.g:227:5: cl= class_ref
                    pass 
                    self._state.following.append(self.FOLLOW_class_ref_in_method_call1650)
                    cl = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_class_ref.add(cl.tree)



                elif alt39 == 2:
                    # Imp.g:227:20: var= variable
                    pass 
                    self._state.following.append(self.FOLLOW_variable_in_method_call1656)
                    var = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_variable.add(var.tree)





                # Imp.g:227:34: ( method_pipe )+
                cnt40 = 0
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 90) :
                        alt40 = 1


                    if alt40 == 1:
                        # Imp.g:227:35: method_pipe
                        pass 
                        self._state.following.append(self.FOLLOW_method_pipe_in_method_call1660)
                        method_pipe166 = self.method_pipe()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_method_pipe.add(method_pipe166.tree)



                    else:
                        if cnt40 >= 1:
                            break #loop40

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(40, self.input)
                        raise eee

                    cnt40 += 1


                # AST Rewrite
                # elements: method_pipe, var, cl
                # token labels: 
                # rule labels: retval, var, cl
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    if var is not None:
                        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var", var.tree)
                    else:
                        stream_var = RewriteRuleSubtreeStream(self._adaptor, "token var", None)

                    if cl is not None:
                        stream_cl = RewriteRuleSubtreeStream(self._adaptor, "rule cl", cl.tree)
                    else:
                        stream_cl = RewriteRuleSubtreeStream(self._adaptor, "token cl", None)


                    root_0 = self._adaptor.nil()
                    # 227:49: -> ^( METHOD ( $cl)? ( $var)? ( method_pipe )+ )
                    # Imp.g:227:52: ^( METHOD ( $cl)? ( $var)? ( method_pipe )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(METHOD, "METHOD")
                    , root_1)

                    # Imp.g:227:62: ( $cl)?
                    if stream_cl.hasNext():
                        self._adaptor.addChild(root_1, stream_cl.nextTree())


                    stream_cl.reset();

                    # Imp.g:227:67: ( $var)?
                    if stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset();

                    # Imp.g:227:72: ( method_pipe )+
                    if not (stream_method_pipe.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_method_pipe.hasNext():
                        self._adaptor.addChild(root_1, stream_method_pipe.nextTree())


                    stream_method_pipe.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "method_call"


    class un_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "un_op"
    # Imp.g:230:1: un_op : 'not' ;
    def un_op(self, ):
        retval = self.un_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal167 = None

        string_literal167_tree = None

        try:
            try:
                # Imp.g:231:2: ( 'not' )
                # Imp.g:231:4: 'not'
                pass 
                root_0 = self._adaptor.nil()


                string_literal167 = self.match(self.input, 81, self.FOLLOW_81_in_un_op1690)
                if self._state.backtracking == 0:
                    string_literal167_tree = self._adaptor.createWithPayload(string_literal167)
                    self._adaptor.addChild(root_0, string_literal167_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "un_op"


    class cmp_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cmp_op"
    # Imp.g:234:1: cmp_op : ( '==' | '!=' | '<=' | '>=' | '<' | '>' | 'is' );
    def cmp_op(self, ):
        retval = self.cmp_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set168 = None

        set168_tree = None

        try:
            try:
                # Imp.g:235:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' | 'is' )
                # Imp.g:
                pass 
                root_0 = self._adaptor.nil()


                set168 = self.input.LT(1)

                if self.input.LA(1) == 50 or self.input.LA(1) == 59 or self.input.LA(1) == 61 or (63 <= self.input.LA(1) <= 65) or self.input.LA(1) == 79:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set168))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "cmp_op"


    class cmp_oper_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cmp_oper"
    # Imp.g:238:1: cmp_oper : ( variable | function_call | method_call | index_lookup | constant | class_ref );
    def cmp_oper(self, ):
        retval = self.cmp_oper_return()
        retval.start = self.input.LT(1)


        root_0 = None

        variable169 = None
        function_call170 = None
        method_call171 = None
        index_lookup172 = None
        constant173 = None
        class_ref174 = None


        try:
            try:
                # Imp.g:239:2: ( variable | function_call | method_call | index_lookup | constant | class_ref )
                alt41 = 6
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # Imp.g:239:4: variable
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_variable_in_cmp_oper1738)
                    variable169 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable169.tree)



                elif alt41 == 2:
                    # Imp.g:239:15: function_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_function_call_in_cmp_oper1742)
                    function_call170 = self.function_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function_call170.tree)



                elif alt41 == 3:
                    # Imp.g:239:31: method_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_method_call_in_cmp_oper1746)
                    method_call171 = self.method_call()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, method_call171.tree)



                elif alt41 == 4:
                    # Imp.g:239:45: index_lookup
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_index_lookup_in_cmp_oper1750)
                    index_lookup172 = self.index_lookup()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, index_lookup172.tree)



                elif alt41 == 5:
                    # Imp.g:239:60: constant
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_constant_in_cmp_oper1754)
                    constant173 = self.constant()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, constant173.tree)



                elif alt41 == 6:
                    # Imp.g:239:71: class_ref
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_class_ref_in_cmp_oper1758)
                    class_ref174 = self.class_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, class_ref174.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "cmp_oper"


    class cmp_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cmp"
    # Imp.g:242:1: cmp : ( ( cmp_oper 'in' )=> cmp_oper 'in' in_oper -> ^( OP 'in' cmp_oper in_oper ) | cmp_oper cmp_op cmp_oper -> ^( OP cmp_op ( cmp_oper )+ ) );
    def cmp(self, ):
        retval = self.cmp_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal176 = None
        cmp_oper175 = None
        in_oper177 = None
        cmp_oper178 = None
        cmp_op179 = None
        cmp_oper180 = None

        string_literal176_tree = None
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_cmp_op = RewriteRuleSubtreeStream(self._adaptor, "rule cmp_op")
        stream_cmp_oper = RewriteRuleSubtreeStream(self._adaptor, "rule cmp_oper")
        stream_in_oper = RewriteRuleSubtreeStream(self._adaptor, "rule in_oper")
        try:
            try:
                # Imp.g:243:2: ( ( cmp_oper 'in' )=> cmp_oper 'in' in_oper -> ^( OP 'in' cmp_oper in_oper ) | cmp_oper cmp_op cmp_oper -> ^( OP cmp_op ( cmp_oper )+ ) )
                alt42 = 2
                LA42 = self.input.LA(1)
                if LA42 in {ID}:
                    LA42_1 = self.input.LA(2)

                    if (self.synpred10_Imp()) :
                        alt42 = 1
                    elif (True) :
                        alt42 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 42, 1, self.input)

                        raise nvae


                elif LA42 in {CLASS_ID}:
                    LA42_2 = self.input.LA(2)

                    if (self.synpred10_Imp()) :
                        alt42 = 1
                    elif (True) :
                        alt42 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 42, 2, self.input)

                        raise nvae


                elif LA42 in {FALSE, FLOAT, INT, ML_STRING, REGEX, STRING, TRUE}:
                    LA42_3 = self.input.LA(2)

                    if (self.synpred10_Imp()) :
                        alt42 = 1
                    elif (True) :
                        alt42 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 42, 3, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae


                if alt42 == 1:
                    # Imp.g:243:4: ( cmp_oper 'in' )=> cmp_oper 'in' in_oper
                    pass 
                    self._state.following.append(self.FOLLOW_cmp_oper_in_cmp1779)
                    cmp_oper175 = self.cmp_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_cmp_oper.add(cmp_oper175.tree)


                    string_literal176 = self.match(self.input, 76, self.FOLLOW_76_in_cmp1781) 
                    if self._state.backtracking == 0:
                        stream_76.add(string_literal176)


                    self._state.following.append(self.FOLLOW_in_oper_in_cmp1783)
                    in_oper177 = self.in_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_in_oper.add(in_oper177.tree)


                    # AST Rewrite
                    # elements: cmp_oper, 76, in_oper
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 243:45: -> ^( OP 'in' cmp_oper in_oper )
                        # Imp.g:243:48: ^( OP 'in' cmp_oper in_oper )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(OP, "OP")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_76.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_cmp_oper.nextTree())

                        self._adaptor.addChild(root_1, stream_in_oper.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt42 == 2:
                    # Imp.g:244:4: cmp_oper cmp_op cmp_oper
                    pass 
                    self._state.following.append(self.FOLLOW_cmp_oper_in_cmp1800)
                    cmp_oper178 = self.cmp_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_cmp_oper.add(cmp_oper178.tree)


                    self._state.following.append(self.FOLLOW_cmp_op_in_cmp1802)
                    cmp_op179 = self.cmp_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_cmp_op.add(cmp_op179.tree)


                    self._state.following.append(self.FOLLOW_cmp_oper_in_cmp1804)
                    cmp_oper180 = self.cmp_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_cmp_oper.add(cmp_oper180.tree)


                    # AST Rewrite
                    # elements: cmp_oper, cmp_op
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 244:29: -> ^( OP cmp_op ( cmp_oper )+ )
                        # Imp.g:244:32: ^( OP cmp_op ( cmp_oper )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(OP, "OP")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_cmp_op.nextTree())

                        # Imp.g:244:44: ( cmp_oper )+
                        if not (stream_cmp_oper.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_cmp_oper.hasNext():
                            self._adaptor.addChild(root_1, stream_cmp_oper.nextTree())


                        stream_cmp_oper.reset()

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "cmp"


    class log_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "log_op"
    # Imp.g:247:1: log_op : ( 'and' | 'or' );
    def log_op(self, ):
        retval = self.log_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set181 = None

        set181_tree = None

        try:
            try:
                # Imp.g:248:2: ( 'and' | 'or' )
                # Imp.g:
                pass 
                root_0 = self._adaptor.nil()


                set181 = self.input.LT(1)

                if self.input.LA(1) == 68 or self.input.LA(1) == 82:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set181))

                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "log_op"


    class in_oper_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "in_oper"
    # Imp.g:251:1: in_oper : ( list_def | variable );
    def in_oper(self, ):
        retval = self.in_oper_return()
        retval.start = self.input.LT(1)


        root_0 = None

        list_def182 = None
        variable183 = None


        try:
            try:
                # Imp.g:252:2: ( list_def | variable )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == 66) :
                    alt43 = 1
                elif (LA43_0 == ID) :
                    alt43 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae


                if alt43 == 1:
                    # Imp.g:252:4: list_def
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_list_def_in_in_oper1843)
                    list_def182 = self.list_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_def182.tree)



                elif alt43 == 2:
                    # Imp.g:252:15: variable
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_variable_in_in_oper1847)
                    variable183 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable183.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "in_oper"


    class log_oper_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "log_oper"
    # Imp.g:255:1: log_oper : ( cmp | TRUE | FALSE );
    def log_oper(self, ):
        retval = self.log_oper_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TRUE185 = None
        FALSE186 = None
        cmp184 = None

        TRUE185_tree = None
        FALSE186_tree = None

        try:
            try:
                # Imp.g:256:2: ( cmp | TRUE | FALSE )
                alt44 = 3
                LA44 = self.input.LA(1)
                if LA44 in {CLASS_ID, FLOAT, ID, INT, ML_STRING, REGEX, STRING}:
                    alt44 = 1
                elif LA44 in {TRUE}:
                    LA44_2 = self.input.LA(2)

                    if (LA44_2 == 50 or LA44_2 == 59 or LA44_2 == 61 or (63 <= LA44_2 <= 65) or LA44_2 == 76 or LA44_2 == 79) :
                        alt44 = 1
                    elif (LA44_2 == EOF or LA44_2 == CLASS_ID or LA44_2 == ENUM_KEY or LA44_2 == ID or LA44_2 == ML_STRING or LA44_2 == 52 or LA44_2 == 68 or LA44_2 == 71 or (73 <= LA44_2 <= 75) or (77 <= LA44_2 <= 78) or LA44_2 == 82 or LA44_2 == 85 or LA44_2 == 91) :
                        alt44 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 44, 2, self.input)

                        raise nvae


                elif LA44 in {FALSE}:
                    LA44_3 = self.input.LA(2)

                    if (LA44_3 == 50 or LA44_3 == 59 or LA44_3 == 61 or (63 <= LA44_3 <= 65) or LA44_3 == 76 or LA44_3 == 79) :
                        alt44 = 1
                    elif (LA44_3 == EOF or LA44_3 == CLASS_ID or LA44_3 == ENUM_KEY or LA44_3 == ID or LA44_3 == ML_STRING or LA44_3 == 52 or LA44_3 == 68 or LA44_3 == 71 or (73 <= LA44_3 <= 75) or (77 <= LA44_3 <= 78) or LA44_3 == 82 or LA44_3 == 85 or LA44_3 == 91) :
                        alt44 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 44, 3, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae


                if alt44 == 1:
                    # Imp.g:256:4: cmp
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cmp_in_log_oper1860)
                    cmp184 = self.cmp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cmp184.tree)



                elif alt44 == 2:
                    # Imp.g:256:10: TRUE
                    pass 
                    root_0 = self._adaptor.nil()


                    TRUE185 = self.match(self.input, TRUE, self.FOLLOW_TRUE_in_log_oper1864)
                    if self._state.backtracking == 0:
                        TRUE185_tree = self._adaptor.createWithPayload(TRUE185)
                        self._adaptor.addChild(root_0, TRUE185_tree)




                elif alt44 == 3:
                    # Imp.g:256:17: FALSE
                    pass 
                    root_0 = self._adaptor.nil()


                    FALSE186 = self.match(self.input, FALSE, self.FOLLOW_FALSE_in_log_oper1868)
                    if self._state.backtracking == 0:
                        FALSE186_tree = self._adaptor.createWithPayload(FALSE186)
                        self._adaptor.addChild(root_0, FALSE186_tree)




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "log_oper"


    class log_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "log_expr"
    # Imp.g:259:1: log_expr : ( ( log_oper log_op )=> log_oper log_op log_expr -> ^( OP log_op log_oper log_expr ) | log_oper );
    def log_expr(self, ):
        retval = self.log_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        log_oper187 = None
        log_op188 = None
        log_expr189 = None
        log_oper190 = None

        stream_log_expr = RewriteRuleSubtreeStream(self._adaptor, "rule log_expr")
        stream_log_oper = RewriteRuleSubtreeStream(self._adaptor, "rule log_oper")
        stream_log_op = RewriteRuleSubtreeStream(self._adaptor, "rule log_op")
        try:
            try:
                # Imp.g:261:2: ( ( log_oper log_op )=> log_oper log_op log_expr -> ^( OP log_op log_oper log_expr ) | log_oper )
                alt45 = 2
                LA45 = self.input.LA(1)
                if LA45 in {ID}:
                    LA45_1 = self.input.LA(2)

                    if (self.synpred11_Imp()) :
                        alt45 = 1
                    elif (True) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 45, 1, self.input)

                        raise nvae


                elif LA45 in {CLASS_ID}:
                    LA45_2 = self.input.LA(2)

                    if (self.synpred11_Imp()) :
                        alt45 = 1
                    elif (True) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 45, 2, self.input)

                        raise nvae


                elif LA45 in {TRUE}:
                    LA45_3 = self.input.LA(2)

                    if (self.synpred11_Imp()) :
                        alt45 = 1
                    elif (True) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 45, 3, self.input)

                        raise nvae


                elif LA45 in {FALSE}:
                    LA45_4 = self.input.LA(2)

                    if (self.synpred11_Imp()) :
                        alt45 = 1
                    elif (True) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 45, 4, self.input)

                        raise nvae


                elif LA45 in {FLOAT, INT, ML_STRING, REGEX, STRING}:
                    LA45_5 = self.input.LA(2)

                    if (self.synpred11_Imp()) :
                        alt45 = 1
                    elif (True) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 45, 5, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae


                if alt45 == 1:
                    # Imp.g:261:4: ( log_oper log_op )=> log_oper log_op log_expr
                    pass 
                    self._state.following.append(self.FOLLOW_log_oper_in_log_expr1889)
                    log_oper187 = self.log_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_log_oper.add(log_oper187.tree)


                    self._state.following.append(self.FOLLOW_log_op_in_log_expr1891)
                    log_op188 = self.log_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_log_op.add(log_op188.tree)


                    self._state.following.append(self.FOLLOW_log_expr_in_log_expr1893)
                    log_expr189 = self.log_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_log_expr.add(log_expr189.tree)


                    # AST Rewrite
                    # elements: log_expr, log_oper, log_op
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 261:50: -> ^( OP log_op log_oper log_expr )
                        # Imp.g:261:53: ^( OP log_op log_oper log_expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(OP, "OP")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_log_op.nextTree())

                        self._adaptor.addChild(root_1, stream_log_oper.nextTree())

                        self._adaptor.addChild(root_1, stream_log_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt45 == 2:
                    # Imp.g:262:4: log_oper
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_log_oper_in_log_expr1910)
                    log_oper190 = self.log_oper()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, log_oper190.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "log_expr"


    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "expression"
    # Imp.g:265:1: expression : ( '(' expression ')' ( log_op expression )? -> ^( OP ( log_op )? ( expression )+ ) | ( log_expr log_op )=> log_expr log_op '(' expression ')' -> ^( OP log_op log_expr expression ) | log_expr );
    def expression(self, ):
        retval = self.expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal191 = None
        char_literal193 = None
        char_literal198 = None
        char_literal200 = None
        expression192 = None
        log_op194 = None
        expression195 = None
        log_expr196 = None
        log_op197 = None
        expression199 = None
        log_expr201 = None

        char_literal191_tree = None
        char_literal193_tree = None
        char_literal198_tree = None
        char_literal200_tree = None
        stream_51 = RewriteRuleTokenStream(self._adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self._adaptor, "token 52")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_log_expr = RewriteRuleSubtreeStream(self._adaptor, "rule log_expr")
        stream_log_op = RewriteRuleSubtreeStream(self._adaptor, "rule log_op")
        try:
            try:
                # Imp.g:266:2: ( '(' expression ')' ( log_op expression )? -> ^( OP ( log_op )? ( expression )+ ) | ( log_expr log_op )=> log_expr log_op '(' expression ')' -> ^( OP log_op log_expr expression ) | log_expr )
                alt47 = 3
                LA47 = self.input.LA(1)
                if LA47 in {51}:
                    alt47 = 1
                elif LA47 in {ID}:
                    LA47_2 = self.input.LA(2)

                    if (self.synpred12_Imp()) :
                        alt47 = 2
                    elif (True) :
                        alt47 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 47, 2, self.input)

                        raise nvae


                elif LA47 in {CLASS_ID}:
                    LA47_3 = self.input.LA(2)

                    if (self.synpred12_Imp()) :
                        alt47 = 2
                    elif (True) :
                        alt47 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 47, 3, self.input)

                        raise nvae


                elif LA47 in {TRUE}:
                    LA47_4 = self.input.LA(2)

                    if (self.synpred12_Imp()) :
                        alt47 = 2
                    elif (True) :
                        alt47 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 47, 4, self.input)

                        raise nvae


                elif LA47 in {FALSE}:
                    LA47_5 = self.input.LA(2)

                    if (self.synpred12_Imp()) :
                        alt47 = 2
                    elif (True) :
                        alt47 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 47, 5, self.input)

                        raise nvae


                elif LA47 in {FLOAT, INT, ML_STRING, REGEX, STRING}:
                    LA47_6 = self.input.LA(2)

                    if (self.synpred12_Imp()) :
                        alt47 = 2
                    elif (True) :
                        alt47 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 47, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae


                if alt47 == 1:
                    # Imp.g:266:4: '(' expression ')' ( log_op expression )?
                    pass 
                    char_literal191 = self.match(self.input, 51, self.FOLLOW_51_in_expression1922) 
                    if self._state.backtracking == 0:
                        stream_51.add(char_literal191)


                    self._state.following.append(self.FOLLOW_expression_in_expression1924)
                    expression192 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression192.tree)


                    char_literal193 = self.match(self.input, 52, self.FOLLOW_52_in_expression1926) 
                    if self._state.backtracking == 0:
                        stream_52.add(char_literal193)


                    # Imp.g:266:23: ( log_op expression )?
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == 68 or LA46_0 == 82) :
                        alt46 = 1
                    if alt46 == 1:
                        # Imp.g:266:24: log_op expression
                        pass 
                        self._state.following.append(self.FOLLOW_log_op_in_expression1929)
                        log_op194 = self.log_op()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_log_op.add(log_op194.tree)


                        self._state.following.append(self.FOLLOW_expression_in_expression1931)
                        expression195 = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(expression195.tree)





                    # AST Rewrite
                    # elements: log_op, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 266:44: -> ^( OP ( log_op )? ( expression )+ )
                        # Imp.g:266:47: ^( OP ( log_op )? ( expression )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(OP, "OP")
                        , root_1)

                        # Imp.g:266:52: ( log_op )?
                        if stream_log_op.hasNext():
                            self._adaptor.addChild(root_1, stream_log_op.nextTree())


                        stream_log_op.reset();

                        # Imp.g:266:60: ( expression )+
                        if not (stream_expression.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset()

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt47 == 2:
                    # Imp.g:267:4: ( log_expr log_op )=> log_expr log_op '(' expression ')'
                    pass 
                    self._state.following.append(self.FOLLOW_log_expr_in_expression1958)
                    log_expr196 = self.log_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_log_expr.add(log_expr196.tree)


                    self._state.following.append(self.FOLLOW_log_op_in_expression1960)
                    log_op197 = self.log_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_log_op.add(log_op197.tree)


                    char_literal198 = self.match(self.input, 51, self.FOLLOW_51_in_expression1962) 
                    if self._state.backtracking == 0:
                        stream_51.add(char_literal198)


                    self._state.following.append(self.FOLLOW_expression_in_expression1964)
                    expression199 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression199.tree)


                    char_literal200 = self.match(self.input, 52, self.FOLLOW_52_in_expression1966) 
                    if self._state.backtracking == 0:
                        stream_52.add(char_literal200)


                    # AST Rewrite
                    # elements: log_op, log_expr, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 267:60: -> ^( OP log_op log_expr expression )
                        # Imp.g:267:63: ^( OP log_op log_expr expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(OP, "OP")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_log_op.nextTree())

                        self._adaptor.addChild(root_1, stream_log_expr.nextTree())

                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt47 == 3:
                    # Imp.g:268:4: log_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_log_expr_in_expression1983)
                    log_expr201 = self.log_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, log_expr201.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                       
            except RecognitionException as re:
            	raise re

        finally:
            pass
        return retval

    # $ANTLR end "expression"

    # $ANTLR start "synpred1_Imp"
    def synpred1_Imp_fragment(self, ):
        # Imp.g:60:4: ( class_ref '(' )
        # Imp.g:60:5: class_ref '('
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_class_ref_in_synpred1_Imp284)
        self.class_ref()

        self._state.following.pop()


        self.match(self.input, 51, self.FOLLOW_51_in_synpred1_Imp286)




    # $ANTLR end "synpred1_Imp"



    # $ANTLR start "synpred2_Imp"
    def synpred2_Imp_fragment(self, ):
        # Imp.g:67:4: ( 'for' )
        # Imp.g:67:5: 'for'
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, 73, self.FOLLOW_73_in_synpred2_Imp326)




    # $ANTLR end "synpred2_Imp"



    # $ANTLR start "synpred3_Imp"
    def synpred3_Imp_fragment(self, ):
        # Imp.g:69:4: ( class_ref '(' )
        # Imp.g:69:5: class_ref '('
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_class_ref_in_synpred3_Imp387)
        self.class_ref()

        self._state.following.pop()


        self.match(self.input, 51, self.FOLLOW_51_in_synpred3_Imp389)




    # $ANTLR end "synpred3_Imp"



    # $ANTLR start "synpred4_Imp"
    def synpred4_Imp_fragment(self, ):
        # Imp.g:130:4: ( INT )
        # Imp.g:130:5: INT
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, INT, self.FOLLOW_INT_in_synpred4_Imp866)




    # $ANTLR end "synpred4_Imp"



    # $ANTLR start "synpred5_Imp"
    def synpred5_Imp_fragment(self, ):
        # Imp.g:131:4: ( INT ':' )
        # Imp.g:131:5: INT ':'
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, INT, self.FOLLOW_INT_in_synpred5_Imp885)


        self.match(self.input, 57, self.FOLLOW_57_in_synpred5_Imp887)




    # $ANTLR end "synpred5_Imp"



    # $ANTLR start "synpred6_Imp"
    def synpred6_Imp_fragment(self, ):
        # Imp.g:132:4: ( INT ':' INT )
        # Imp.g:132:5: INT ':' INT
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, INT, self.FOLLOW_INT_in_synpred6_Imp910)


        self.match(self.input, 57, self.FOLLOW_57_in_synpred6_Imp912)


        self.match(self.input, INT, self.FOLLOW_INT_in_synpred6_Imp914)




    # $ANTLR end "synpred6_Imp"



    # $ANTLR start "synpred7_Imp"
    def synpred7_Imp_fragment(self, ):
        # Imp.g:133:4: ( ':' INT )
        # Imp.g:133:5: ':' INT
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, 57, self.FOLLOW_57_in_synpred7_Imp939)


        self.match(self.input, INT, self.FOLLOW_INT_in_synpred7_Imp941)




    # $ANTLR end "synpred7_Imp"



    # $ANTLR start "synpred8_Imp"
    def synpred8_Imp_fragment(self, ):
        # Imp.g:158:4: ( ns_ref '(' )
        # Imp.g:158:5: ns_ref '('
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_ns_ref_in_synpred8_Imp1107)
        self.ns_ref()

        self._state.following.pop()


        self.match(self.input, 51, self.FOLLOW_51_in_synpred8_Imp1109)




    # $ANTLR end "synpred8_Imp"



    # $ANTLR start "synpred9_Imp"
    def synpred9_Imp_fragment(self, ):
        # Imp.g:162:4: ( '{' )
        # Imp.g:162:5: '{'
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, 89, self.FOLLOW_89_in_synpred9_Imp1135)




    # $ANTLR end "synpred9_Imp"



    # $ANTLR start "synpred10_Imp"
    def synpred10_Imp_fragment(self, ):
        # Imp.g:243:4: ( cmp_oper 'in' )
        # Imp.g:243:5: cmp_oper 'in'
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_cmp_oper_in_synpred10_Imp1772)
        self.cmp_oper()

        self._state.following.pop()


        self.match(self.input, 76, self.FOLLOW_76_in_synpred10_Imp1774)




    # $ANTLR end "synpred10_Imp"



    # $ANTLR start "synpred11_Imp"
    def synpred11_Imp_fragment(self, ):
        # Imp.g:261:4: ( log_oper log_op )
        # Imp.g:261:5: log_oper log_op
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_log_oper_in_synpred11_Imp1882)
        self.log_oper()

        self._state.following.pop()


        self._state.following.append(self.FOLLOW_log_op_in_synpred11_Imp1884)
        self.log_op()

        self._state.following.pop()




    # $ANTLR end "synpred11_Imp"



    # $ANTLR start "synpred12_Imp"
    def synpred12_Imp_fragment(self, ):
        # Imp.g:267:4: ( log_expr log_op )
        # Imp.g:267:5: log_expr log_op
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_log_expr_in_synpred12_Imp1951)
        self.log_expr()

        self._state.following.pop()


        self._state.following.append(self.FOLLOW_log_op_in_synpred12_Imp1953)
        self.log_op()

        self._state.following.pop()




    # $ANTLR end "synpred12_Imp"




    def synpred11_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred8_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred5_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred5_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred12_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred12_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred3_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred6_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred6_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred2_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred10_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred10_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred9_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred7_Imp(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred7_Imp_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #1

    DFA1_eot = DFA.unpack(
        "\11\uffff"
        )

    DFA1_eof = DFA.unpack(
        "\1\1\10\uffff"
        )

    DFA1_min = DFA.unpack(
        "\1\10\2\uffff\1\63\1\34\2\uffff\1\10\1\63"
        )

    DFA1_max = DFA.unpack(
        "\1\125\2\uffff\2\132\2\uffff\1\34\1\132"
        )

    DFA1_accept = DFA.unpack(
        "\1\uffff\1\4\1\1\2\uffff\1\2\1\3\2\uffff"
        )

    DFA1_special = DFA.unpack(
        "\11\uffff"
        )


    DFA1_transition = [
        DFA.unpack("\1\4\12\uffff\1\5\10\uffff\1\3\6\uffff\1\6\43\uffff\1"
        "\2\1\uffff\1\5\2\2\1\uffff\1\5\1\2\6\uffff\1\2"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\5\4\uffff\1\5\1\uffff\1\7\3\uffff\1\5\33\uffff\1"
        "\5"),
        DFA.unpack("\1\2\26\uffff\1\5\46\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\4\23\uffff\1\10"),
        DFA.unpack("\1\5\4\uffff\1\5\1\uffff\1\7\3\uffff\1\5\33\uffff\1"
        "\5")
    ]

    # class definition for DFA #1

    class DFA1(DFA):
        pass


    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        "\7\uffff"
        )

    DFA4_eof = DFA.unpack(
        "\1\uffff\2\3\3\uffff\1\3"
        )

    DFA4_min = DFA.unpack(
        "\3\10\1\uffff\1\10\1\uffff\1\10"
        )

    DFA4_max = DFA.unpack(
        "\1\131\2\132\1\uffff\1\34\1\uffff\1\132"
        )

    DFA4_accept = DFA.unpack(
        "\3\uffff\1\2\1\uffff\1\1\1\uffff"
        )

    DFA4_special = DFA.unpack(
        "\2\uffff\1\0\4\uffff"
        )


    DFA4_transition = [
        DFA.unpack("\1\2\16\uffff\2\3\3\uffff\1\1\2\uffff\1\3\3\uffff\1\3"
        "\7\uffff\1\3\1\uffff\2\3\23\uffff\1\3\26\uffff\1\3"),
        DFA.unpack("\1\3\12\uffff\1\3\10\uffff\1\3\6\uffff\1\3\17\uffff"
        "\1\3\4\uffff\1\3\1\uffff\1\4\13\uffff\2\3\1\uffff\3\3\1\uffff\2"
        "\3\6\uffff\1\3\4\uffff\1\3"),
        DFA.unpack("\1\3\12\uffff\1\3\10\uffff\1\3\6\uffff\1\3\17\uffff"
        "\1\5\16\uffff\1\3\3\uffff\2\3\1\uffff\3\3\1\uffff\2\3\6\uffff\1"
        "\3\4\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack("\1\2\23\uffff\1\6"),
        DFA.unpack(""),
        DFA.unpack("\1\3\12\uffff\1\3\10\uffff\1\3\6\uffff\1\3\17\uffff"
        "\1\3\4\uffff\1\3\1\uffff\1\4\13\uffff\2\3\1\uffff\3\3\1\uffff\2"
        "\3\6\uffff\1\3\4\uffff\1\3")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA4_2 = input.LA(1)

                 
                index4_2 = input.index()
                input.rewind()

                s = -1
                if (LA4_2 == 51) and (self.synpred1_Imp()):
                    s = 5

                elif (LA4_2 == EOF or LA4_2 == CLASS_ID or LA4_2 == ENUM_KEY or LA4_2 == ID or LA4_2 == ML_STRING or LA4_2 == 66 or (70 <= LA4_2 <= 71) or (73 <= LA4_2 <= 75) or (77 <= LA4_2 <= 78) or LA4_2 == 85 or LA4_2 == 90):
                    s = 3

                 
                input.seek(index4_2)

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 4, _s, input)
            self_.error(nvae)
            raise nvae

    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        "\16\uffff"
        )

    DFA6_eof = DFA.unpack(
        "\16\uffff"
        )

    DFA6_min = DFA.unpack(
        "\1\10\2\uffff\2\63\1\uffff\1\10\1\34\4\uffff\1\63\1\70"
        )

    DFA6_max = DFA.unpack(
        "\1\115\2\uffff\2\132\1\uffff\2\34\4\uffff\2\132"
        )

    DFA6_accept = DFA.unpack(
        "\1\uffff\1\1\1\2\2\uffff\1\7\2\uffff\1\3\1\5\1\6\1\4\2\uffff"
        )

    DFA6_special = DFA.unpack(
        "\1\0\3\uffff\1\1\11\uffff"
        )


    DFA6_transition = [
        DFA.unpack("\1\4\12\uffff\1\5\10\uffff\1\3\54\uffff\1\2\3\uffff\1"
        "\1"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\11\4\uffff\1\7\1\uffff\1\6\3\uffff\1\10\33\uffff"
        "\1\12"),
        DFA.unpack("\1\13\46\uffff\1\12"),
        DFA.unpack(""),
        DFA.unpack("\1\4\23\uffff\1\14"),
        DFA.unpack("\1\15"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\11\4\uffff\1\7\1\uffff\1\6\3\uffff\1\10\33\uffff"
        "\1\12"),
        DFA.unpack("\1\7\5\uffff\1\10\33\uffff\1\12")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA6_0 = input.LA(1)

                 
                index6_0 = input.index()
                input.rewind()

                s = -1
                if (LA6_0 == 77):
                    s = 1

                elif (LA6_0 == 73) and (self.synpred2_Imp()):
                    s = 2

                elif (LA6_0 == ID):
                    s = 3

                elif (LA6_0 == CLASS_ID):
                    s = 4

                elif (LA6_0 == ENUM_KEY):
                    s = 5

                 
                input.seek(index6_0)

                if s >= 0:
                    return s
            elif s == 1: 
                LA6_4 = input.LA(1)

                 
                index6_4 = input.index()
                input.rewind()

                s = -1
                if (LA6_4 == 51) and (self.synpred3_Imp()):
                    s = 11

                elif (LA6_4 == 90):
                    s = 10

                 
                input.seek(index6_4)

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 6, _s, input)
            self_.error(nvae)
            raise nvae

    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        "\5\uffff"
        )

    DFA5_eof = DFA.unpack(
        "\5\uffff"
        )

    DFA5_min = DFA.unpack(
        "\1\10\1\70\1\uffff\1\10\1\uffff"
        )

    DFA5_max = DFA.unpack(
        "\1\34\1\72\1\uffff\1\34\1\uffff"
        )

    DFA5_accept = DFA.unpack(
        "\2\uffff\1\2\1\uffff\1\1"
        )

    DFA5_special = DFA.unpack(
        "\5\uffff"
        )


    DFA5_transition = [
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("\2\4\1\3"),
        DFA.unpack(""),
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        "\10\uffff"
        )

    DFA9_eof = DFA.unpack(
        "\10\uffff"
        )

    DFA9_min = DFA.unpack(
        "\1\10\2\63\1\10\3\uffff\1\63"
        )

    DFA9_max = DFA.unpack(
        "\1\34\2\132\1\34\3\uffff\1\132"
        )

    DFA9_accept = DFA.unpack(
        "\4\uffff\1\1\1\2\1\3\1\uffff"
        )

    DFA9_special = DFA.unpack(
        "\10\uffff"
        )


    DFA9_transition = [
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("\1\4\4\uffff\1\5\1\uffff\1\3\37\uffff\1\5"),
        DFA.unpack("\1\6\46\uffff\1\5"),
        DFA.unpack("\1\2\23\uffff\1\7"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\4\4\uffff\1\5\1\uffff\1\3\37\uffff\1\5")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        "\17\uffff"
        )

    DFA21_eof = DFA.unpack(
        "\3\uffff\1\11\1\14\10\uffff\2\11"
        )

    DFA21_min = DFA.unpack(
        "\1\10\2\uffff\2\10\1\uffff\1\10\1\uffff\1\34\4\uffff\2\10"
        )

    DFA21_max = DFA.unpack(
        "\1\131\2\uffff\2\132\1\uffff\1\34\1\uffff\1\34\4\uffff\2\132"
        )

    DFA21_accept = DFA.unpack(
        "\1\uffff\1\1\1\2\2\uffff\1\10\1\uffff\1\4\1\uffff\1\6\1\7\1\3\1"
        "\5\2\uffff"
        )

    DFA21_special = DFA.unpack(
        "\1\0\2\uffff\1\2\11\uffff\1\1\1\uffff"
        )


    DFA21_transition = [
        DFA.unpack("\1\4\16\uffff\2\1\3\uffff\1\3\2\uffff\1\1\3\uffff\1\1"
        "\7\uffff\1\1\1\uffff\2\1\23\uffff\1\2\26\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\11\12\uffff\1\11\10\uffff\1\11\6\uffff\1\11\17\uffff"
        "\1\7\2\11\2\uffff\1\10\1\uffff\1\6\10\uffff\1\11\2\uffff\2\11\1"
        "\uffff\3\11\1\uffff\2\11\6\uffff\1\11\4\uffff\1\12"),
        DFA.unpack("\1\14\12\uffff\1\14\10\uffff\1\14\6\uffff\1\14\20\uffff"
        "\2\14\14\uffff\1\13\1\14\2\uffff\2\14\1\uffff\3\14\1\uffff\2\14"
        "\6\uffff\1\14\4\uffff\1\12"),
        DFA.unpack(""),
        DFA.unpack("\1\4\23\uffff\1\15"),
        DFA.unpack(""),
        DFA.unpack("\1\16"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\11\12\uffff\1\11\10\uffff\1\11\6\uffff\1\11\17\uffff"
        "\1\7\2\11\2\uffff\1\10\1\uffff\1\6\10\uffff\1\11\2\uffff\2\11\1"
        "\uffff\3\11\1\uffff\2\11\6\uffff\1\11\4\uffff\1\12"),
        DFA.unpack("\1\11\12\uffff\1\11\10\uffff\1\11\6\uffff\1\11\20\uffff"
        "\2\11\2\uffff\1\10\12\uffff\1\11\2\uffff\2\11\1\uffff\3\11\1\uffff"
        "\2\11\6\uffff\1\11\4\uffff\1\12")
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA21_0 = input.LA(1)

                 
                index21_0 = input.index()
                input.rewind()

                s = -1
                if ((FALSE <= LA21_0 <= FLOAT) or LA21_0 == INT or LA21_0 == ML_STRING or LA21_0 == REGEX or (STRING <= LA21_0 <= TRUE)):
                    s = 1

                elif (LA21_0 == 66):
                    s = 2

                elif (LA21_0 == ID):
                    s = 3

                elif (LA21_0 == CLASS_ID):
                    s = 4

                elif (LA21_0 == 89) and (self.synpred9_Imp()):
                    s = 5

                 
                input.seek(index21_0)

                if s >= 0:
                    return s
            elif s == 1: 
                LA21_13 = input.LA(1)

                 
                index21_13 = input.index()
                input.rewind()

                s = -1
                if (LA21_13 == 58):
                    s = 6

                elif (LA21_13 == 51) and (self.synpred8_Imp()):
                    s = 7

                elif (LA21_13 == 56):
                    s = 8

                elif (LA21_13 == EOF or LA21_13 == CLASS_ID or LA21_13 == ENUM_KEY or LA21_13 == ID or LA21_13 == ML_STRING or (52 <= LA21_13 <= 53) or LA21_13 == 67 or (70 <= LA21_13 <= 71) or (73 <= LA21_13 <= 75) or (77 <= LA21_13 <= 78) or LA21_13 == 85):
                    s = 9

                elif (LA21_13 == 90):
                    s = 10

                 
                input.seek(index21_13)

                if s >= 0:
                    return s
            elif s == 2: 
                LA21_3 = input.LA(1)

                 
                index21_3 = input.index()
                input.rewind()

                s = -1
                if (LA21_3 == 58):
                    s = 6

                elif (LA21_3 == 51) and (self.synpred8_Imp()):
                    s = 7

                elif (LA21_3 == 56):
                    s = 8

                elif (LA21_3 == EOF or LA21_3 == CLASS_ID or LA21_3 == ENUM_KEY or LA21_3 == ID or LA21_3 == ML_STRING or (52 <= LA21_3 <= 53) or LA21_3 == 67 or (70 <= LA21_3 <= 71) or (73 <= LA21_3 <= 75) or (77 <= LA21_3 <= 78) or LA21_3 == 85):
                    s = 9

                elif (LA21_3 == 90):
                    s = 10

                 
                input.seek(index21_3)

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 21, _s, input)
            self_.error(nvae)
            raise nvae

    # lookup tables for DFA #28

    DFA28_eot = DFA.unpack(
        "\6\uffff"
        )

    DFA28_eof = DFA.unpack(
        "\6\uffff"
        )

    DFA28_min = DFA.unpack(
        "\1\10\1\34\1\uffff\1\10\1\uffff\1\34"
        )

    DFA28_max = DFA.unpack(
        "\1\34\1\72\1\uffff\1\34\1\uffff\1\72"
        )

    DFA28_accept = DFA.unpack(
        "\2\uffff\1\2\1\uffff\1\1\1\uffff"
        )

    DFA28_special = DFA.unpack(
        "\6\uffff"
        )


    DFA28_transition = [
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("\1\4\35\uffff\1\3"),
        DFA.unpack(""),
        DFA.unpack("\1\2\23\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack("\1\4\35\uffff\1\3")
    ]

    # class definition for DFA #28

    class DFA28(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        "\5\uffff"
        )

    DFA39_eof = DFA.unpack(
        "\5\uffff"
        )

    DFA39_min = DFA.unpack(
        "\1\10\1\70\1\uffff\1\10\1\uffff"
        )

    DFA39_max = DFA.unpack(
        "\1\34\1\132\1\uffff\1\34\1\uffff"
        )

    DFA39_accept = DFA.unpack(
        "\2\uffff\1\1\1\uffff\1\2"
        )

    DFA39_special = DFA.unpack(
        "\5\uffff"
        )


    DFA39_transition = [
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("\1\4\1\uffff\1\3\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack("\1\2\23\uffff\1\1"),
        DFA.unpack("")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        "\15\uffff"
        )

    DFA41_eof = DFA.unpack(
        "\1\uffff\1\6\1\12\10\uffff\2\6"
        )

    DFA41_min = DFA.unpack(
        "\3\10\1\uffff\1\10\1\34\5\uffff\2\10"
        )

    DFA41_max = DFA.unpack(
        "\1\56\2\133\1\uffff\2\34\5\uffff\2\133"
        )

    DFA41_accept = DFA.unpack(
        "\3\uffff\1\5\2\uffff\1\1\1\2\1\3\1\4\1\6\2\uffff"
        )

    DFA41_special = DFA.unpack(
        "\15\uffff"
        )


    DFA41_transition = [
        DFA.unpack("\1\2\16\uffff\2\3\3\uffff\1\1\2\uffff\1\3\3\uffff\1\3"
        "\7\uffff\1\3\1\uffff\2\3"),
        DFA.unpack("\1\6\12\uffff\1\6\10\uffff\1\6\6\uffff\1\6\16\uffff"
        "\1\6\1\7\1\6\3\uffff\1\5\1\uffff\1\4\1\6\1\uffff\1\6\1\uffff\3\6"
        "\2\uffff\1\6\2\uffff\1\6\1\uffff\7\6\2\uffff\1\6\2\uffff\1\6\4\uffff"
        "\1\10\1\6"),
        DFA.unpack("\1\12\12\uffff\1\12\10\uffff\1\12\6\uffff\1\12\16\uffff"
        "\1\12\1\uffff\1\12\6\uffff\1\12\1\uffff\1\12\1\uffff\3\12\1\11\1"
        "\uffff\1\12\2\uffff\1\12\1\uffff\7\12\2\uffff\1\12\2\uffff\1\12"
        "\4\uffff\1\10\1\12"),
        DFA.unpack(""),
        DFA.unpack("\1\2\23\uffff\1\13"),
        DFA.unpack("\1\14"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\6\12\uffff\1\6\10\uffff\1\6\6\uffff\1\6\16\uffff"
        "\1\6\1\7\1\6\3\uffff\1\5\1\uffff\1\4\1\6\1\uffff\1\6\1\uffff\3\6"
        "\2\uffff\1\6\2\uffff\1\6\1\uffff\7\6\2\uffff\1\6\2\uffff\1\6\4\uffff"
        "\1\10\1\6"),
        DFA.unpack("\1\6\12\uffff\1\6\10\uffff\1\6\6\uffff\1\6\16\uffff"
        "\1\6\1\uffff\1\6\3\uffff\1\5\2\uffff\1\6\1\uffff\1\6\1\uffff\3\6"
        "\2\uffff\1\6\2\uffff\1\6\1\uffff\7\6\2\uffff\1\6\2\uffff\1\6\4\uffff"
        "\1\10\1\6")
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass


 

    FOLLOW_def_statement_in_main172 = frozenset([1, 8, 19, 28, 35, 71, 73, 74, 75, 77, 78, 85])
    FOLLOW_top_statement_in_main176 = frozenset([1, 8, 19, 28, 35, 71, 73, 74, 75, 77, 78, 85])
    FOLLOW_ML_STRING_in_main180 = frozenset([1, 8, 19, 28, 35, 71, 73, 74, 75, 77, 78, 85])
    FOLLOW_typedef_in_def_statement208 = frozenset([1])
    FOLLOW_entity_def_in_def_statement212 = frozenset([1])
    FOLLOW_implementation_def_in_def_statement216 = frozenset([1])
    FOLLOW_relation_in_def_statement220 = frozenset([1])
    FOLLOW_index_in_def_statement224 = frozenset([1])
    FOLLOW_implement_def_in_def_statement228 = frozenset([1])
    FOLLOW_78_in_index240 = frozenset([8, 28])
    FOLLOW_class_ref_in_index242 = frozenset([51])
    FOLLOW_51_in_index244 = frozenset([28])
    FOLLOW_ID_in_index246 = frozenset([52, 53])
    FOLLOW_53_in_index249 = frozenset([28])
    FOLLOW_ID_in_index251 = frozenset([52, 53])
    FOLLOW_52_in_index255 = frozenset([1])
    FOLLOW_anon_ctor_in_rhs291 = frozenset([1])
    FOLLOW_operand_in_rhs296 = frozenset([1])
    FOLLOW_77_in_top_statement309 = frozenset([28])
    FOLLOW_ns_ref_in_top_statement311 = frozenset([1])
    FOLLOW_73_in_top_statement331 = frozenset([28])
    FOLLOW_ID_in_top_statement333 = frozenset([76])
    FOLLOW_76_in_top_statement335 = frozenset([8, 28])
    FOLLOW_variable_in_top_statement338 = frozenset([57])
    FOLLOW_class_ref_in_top_statement342 = frozenset([57])
    FOLLOW_implementation_in_top_statement346 = frozenset([1])
    FOLLOW_variable_in_top_statement367 = frozenset([62])
    FOLLOW_62_in_top_statement369 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 66, 89])
    FOLLOW_rhs_in_top_statement371 = frozenset([1])
    FOLLOW_anon_ctor_in_top_statement394 = frozenset([1])
    FOLLOW_function_call_in_top_statement407 = frozenset([1])
    FOLLOW_method_call_in_top_statement412 = frozenset([1])
    FOLLOW_enum_stmt_in_top_statement417 = frozenset([1])
    FOLLOW_ENUM_KEY_in_enum_stmt445 = frozenset([28])
    FOLLOW_ns_ref_in_enum_stmt447 = frozenset([88])
    FOLLOW_88_in_enum_stmt449 = frozenset([83])
    FOLLOW_83_in_enum_stmt451 = frozenset([45, 84])
    FOLLOW_enum_parent_in_enum_stmt453 = frozenset([69])
    FOLLOW_69_in_enum_stmt455 = frozenset([45])
    FOLLOW_STRING_in_enum_stmt457 = frozenset([1, 53])
    FOLLOW_53_in_enum_stmt460 = frozenset([45])
    FOLLOW_STRING_in_enum_stmt462 = frozenset([1, 53])
    FOLLOW_constructor_in_anon_ctor491 = frozenset([1, 57])
    FOLLOW_implementation_in_anon_ctor493 = frozenset([1])
    FOLLOW_constructor_in_lambda_ctor517 = frozenset([1])
    FOLLOW_ID_in_lambda_func537 = frozenset([90])
    FOLLOW_90_in_lambda_func539 = frozenset([8, 28])
    FOLLOW_function_call_in_lambda_func542 = frozenset([1])
    FOLLOW_method_call_in_lambda_func546 = frozenset([1])
    FOLLOW_lambda_ctor_in_lambda_func550 = frozenset([1])
    FOLLOW_75_in_implementation_def579 = frozenset([28])
    FOLLOW_ID_in_implementation_def581 = frozenset([57, 73])
    FOLLOW_73_in_implementation_def584 = frozenset([8, 28])
    FOLLOW_class_ref_in_implementation_def586 = frozenset([57])
    FOLLOW_implementation_in_implementation_def590 = frozenset([1])
    FOLLOW_74_in_implement_def615 = frozenset([8, 28])
    FOLLOW_class_ref_in_implement_def617 = frozenset([86])
    FOLLOW_86_in_implement_def619 = frozenset([28])
    FOLLOW_ns_ref_in_implement_def621 = frozenset([1, 53, 87])
    FOLLOW_53_in_implement_def624 = frozenset([28])
    FOLLOW_ns_ref_in_implement_def626 = frozenset([1, 53, 87])
    FOLLOW_87_in_implement_def631 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_expression_in_implement_def633 = frozenset([1])
    FOLLOW_57_in_implementation665 = frozenset([8, 19, 28, 35, 70, 73, 77])
    FOLLOW_ML_STRING_in_implementation667 = frozenset([8, 19, 28, 70, 73, 77])
    FOLLOW_statement_in_implementation670 = frozenset([8, 19, 28, 70, 73, 77])
    FOLLOW_70_in_implementation673 = frozenset([1])
    FOLLOW_top_statement_in_statement693 = frozenset([1])
    FOLLOW_ID_in_parameter713 = frozenset([62])
    FOLLOW_62_in_parameter715 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 66, 89])
    FOLLOW_operand_in_parameter717 = frozenset([1])
    FOLLOW_class_ref_in_constructor738 = frozenset([51])
    FOLLOW_51_in_constructor740 = frozenset([28, 52])
    FOLLOW_param_list_in_constructor742 = frozenset([52])
    FOLLOW_52_in_constructor745 = frozenset([1])
    FOLLOW_parameter_in_param_list770 = frozenset([1, 53])
    FOLLOW_53_in_param_list773 = frozenset([28])
    FOLLOW_parameter_in_param_list775 = frozenset([1, 53])
    FOLLOW_53_in_param_list779 = frozenset([1])
    FOLLOW_85_in_typedef800 = frozenset([28])
    FOLLOW_ID_in_typedef802 = frozenset([69])
    FOLLOW_69_in_typedef804 = frozenset([28])
    FOLLOW_ns_ref_in_typedef806 = frozenset([80])
    FOLLOW_80_in_typedef808 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_REGEX_in_typedef811 = frozenset([1])
    FOLLOW_expression_in_typedef815 = frozenset([1])
    FOLLOW_85_in_typedef837 = frozenset([8])
    FOLLOW_CLASS_ID_in_typedef839 = frozenset([69])
    FOLLOW_69_in_typedef841 = frozenset([8, 28])
    FOLLOW_constructor_in_typedef843 = frozenset([1])
    FOLLOW_INT_in_multiplicity_body871 = frozenset([1])
    FOLLOW_INT_in_multiplicity_body892 = frozenset([57])
    FOLLOW_57_in_multiplicity_body894 = frozenset([1])
    FOLLOW_INT_in_multiplicity_body919 = frozenset([57])
    FOLLOW_57_in_multiplicity_body921 = frozenset([31])
    FOLLOW_INT_in_multiplicity_body923 = frozenset([1])
    FOLLOW_57_in_multiplicity_body946 = frozenset([31])
    FOLLOW_INT_in_multiplicity_body948 = frozenset([1])
    FOLLOW_66_in_multiplicity970 = frozenset([31, 57])
    FOLLOW_multiplicity_body_in_multiplicity972 = frozenset([67])
    FOLLOW_67_in_multiplicity974 = frozenset([1])
    FOLLOW_class_ref_in_relation_end989 = frozenset([28])
    FOLLOW_ID_in_relation_end991 = frozenset([1])
    FOLLOW_relation_end_in_relation1032 = frozenset([66])
    FOLLOW_multiplicity_in_relation1036 = frozenset([54, 55, 60])
    FOLLOW_relation_link_in_relation1039 = frozenset([66])
    FOLLOW_multiplicity_in_relation1044 = frozenset([8, 28])
    FOLLOW_relation_end_in_relation1048 = frozenset([1])
    FOLLOW_constant_in_operand1091 = frozenset([1])
    FOLLOW_list_def_in_operand1096 = frozenset([1])
    FOLLOW_index_lookup_in_operand1101 = frozenset([1])
    FOLLOW_function_call_in_operand1114 = frozenset([1])
    FOLLOW_class_ref_in_operand1119 = frozenset([1])
    FOLLOW_variable_in_operand1124 = frozenset([1])
    FOLLOW_method_call_in_operand1129 = frozenset([1])
    FOLLOW_89_in_operand1140 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_expression_in_operand1142 = frozenset([91])
    FOLLOW_91_in_operand1144 = frozenset([1])
    FOLLOW_66_in_list_def1210 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 66, 89])
    FOLLOW_operand_in_list_def1212 = frozenset([53, 67])
    FOLLOW_53_in_list_def1215 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 66, 89])
    FOLLOW_operand_in_list_def1217 = frozenset([53, 67])
    FOLLOW_53_in_list_def1221 = frozenset([67])
    FOLLOW_67_in_list_def1224 = frozenset([1])
    FOLLOW_param_list_in_index_arg1245 = frozenset([1])
    FOLLOW_class_ref_in_index_lookup1258 = frozenset([66])
    FOLLOW_66_in_index_lookup1260 = frozenset([28])
    FOLLOW_index_arg_in_index_lookup1262 = frozenset([67])
    FOLLOW_67_in_index_lookup1264 = frozenset([1])
    FOLLOW_71_in_entity_def1286 = frozenset([8])
    FOLLOW_CLASS_ID_in_entity_def1288 = frozenset([57, 72])
    FOLLOW_72_in_entity_def1291 = frozenset([8, 28])
    FOLLOW_class_ref_in_entity_def1293 = frozenset([53, 57])
    FOLLOW_53_in_entity_def1296 = frozenset([8, 28])
    FOLLOW_class_ref_in_entity_def1298 = frozenset([53, 57])
    FOLLOW_57_in_entity_def1305 = frozenset([8, 28, 35, 70])
    FOLLOW_ML_STRING_in_entity_def1307 = frozenset([8, 28, 70])
    FOLLOW_entity_body_in_entity_def1311 = frozenset([8, 28, 70])
    FOLLOW_70_in_entity_def1315 = frozenset([1])
    FOLLOW_ns_ref_in_type1357 = frozenset([1])
    FOLLOW_class_ref_in_type1361 = frozenset([1])
    FOLLOW_type_in_entity_body1372 = frozenset([28])
    FOLLOW_ID_in_entity_body1374 = frozenset([1, 62])
    FOLLOW_62_in_entity_body1377 = frozenset([23, 24, 31, 35, 43, 45, 46])
    FOLLOW_constant_in_entity_body1379 = frozenset([1])
    FOLLOW_ID_in_ns_ref1406 = frozenset([1, 58])
    FOLLOW_58_in_ns_ref1409 = frozenset([28])
    FOLLOW_ID_in_ns_ref1411 = frozenset([1, 58])
    FOLLOW_ID_in_class_ref1440 = frozenset([58])
    FOLLOW_58_in_class_ref1442 = frozenset([8, 28])
    FOLLOW_CLASS_ID_in_class_ref1446 = frozenset([1])
    FOLLOW_ID_in_variable1480 = frozenset([58])
    FOLLOW_58_in_variable1482 = frozenset([28])
    FOLLOW_ID_in_variable1488 = frozenset([1, 56])
    FOLLOW_56_in_variable1491 = frozenset([28])
    FOLLOW_ID_in_variable1495 = frozenset([1, 56])
    FOLLOW_operand_in_arg_list1534 = frozenset([1, 53])
    FOLLOW_53_in_arg_list1537 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 66, 89])
    FOLLOW_operand_in_arg_list1539 = frozenset([1, 53])
    FOLLOW_53_in_arg_list1543 = frozenset([1])
    FOLLOW_ns_ref_in_function_call1565 = frozenset([51])
    FOLLOW_51_in_function_call1567 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 52, 66, 89])
    FOLLOW_call_arg_in_function_call1569 = frozenset([52])
    FOLLOW_52_in_function_call1572 = frozenset([1])
    FOLLOW_arg_list_in_call_arg1600 = frozenset([1])
    FOLLOW_90_in_method_pipe1611 = frozenset([28])
    FOLLOW_ns_ref_in_method_pipe1613 = frozenset([1, 51])
    FOLLOW_51_in_method_pipe1616 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 52, 66, 89])
    FOLLOW_call_arg_in_method_pipe1618 = frozenset([52])
    FOLLOW_52_in_method_pipe1621 = frozenset([1])
    FOLLOW_class_ref_in_method_call1650 = frozenset([90])
    FOLLOW_variable_in_method_call1656 = frozenset([90])
    FOLLOW_method_pipe_in_method_call1660 = frozenset([1, 90])
    FOLLOW_81_in_un_op1690 = frozenset([1])
    FOLLOW_variable_in_cmp_oper1738 = frozenset([1])
    FOLLOW_function_call_in_cmp_oper1742 = frozenset([1])
    FOLLOW_method_call_in_cmp_oper1746 = frozenset([1])
    FOLLOW_index_lookup_in_cmp_oper1750 = frozenset([1])
    FOLLOW_constant_in_cmp_oper1754 = frozenset([1])
    FOLLOW_class_ref_in_cmp_oper1758 = frozenset([1])
    FOLLOW_cmp_oper_in_cmp1779 = frozenset([76])
    FOLLOW_76_in_cmp1781 = frozenset([28, 66])
    FOLLOW_in_oper_in_cmp1783 = frozenset([1])
    FOLLOW_cmp_oper_in_cmp1800 = frozenset([50, 59, 61, 63, 64, 65, 79])
    FOLLOW_cmp_op_in_cmp1802 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46])
    FOLLOW_cmp_oper_in_cmp1804 = frozenset([1])
    FOLLOW_list_def_in_in_oper1843 = frozenset([1])
    FOLLOW_variable_in_in_oper1847 = frozenset([1])
    FOLLOW_cmp_in_log_oper1860 = frozenset([1])
    FOLLOW_TRUE_in_log_oper1864 = frozenset([1])
    FOLLOW_FALSE_in_log_oper1868 = frozenset([1])
    FOLLOW_log_oper_in_log_expr1889 = frozenset([68, 82])
    FOLLOW_log_op_in_log_expr1891 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46])
    FOLLOW_log_expr_in_log_expr1893 = frozenset([1])
    FOLLOW_log_oper_in_log_expr1910 = frozenset([1])
    FOLLOW_51_in_expression1922 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_expression_in_expression1924 = frozenset([52])
    FOLLOW_52_in_expression1926 = frozenset([1, 68, 82])
    FOLLOW_log_op_in_expression1929 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_expression_in_expression1931 = frozenset([1])
    FOLLOW_log_expr_in_expression1958 = frozenset([68, 82])
    FOLLOW_log_op_in_expression1960 = frozenset([51])
    FOLLOW_51_in_expression1962 = frozenset([8, 23, 24, 28, 31, 35, 43, 45, 46, 51])
    FOLLOW_expression_in_expression1964 = frozenset([52])
    FOLLOW_52_in_expression1966 = frozenset([1])
    FOLLOW_log_expr_in_expression1983 = frozenset([1])
    FOLLOW_class_ref_in_synpred1_Imp284 = frozenset([51])
    FOLLOW_51_in_synpred1_Imp286 = frozenset([1])
    FOLLOW_73_in_synpred2_Imp326 = frozenset([1])
    FOLLOW_class_ref_in_synpred3_Imp387 = frozenset([51])
    FOLLOW_51_in_synpred3_Imp389 = frozenset([1])
    FOLLOW_INT_in_synpred4_Imp866 = frozenset([1])
    FOLLOW_INT_in_synpred5_Imp885 = frozenset([57])
    FOLLOW_57_in_synpred5_Imp887 = frozenset([1])
    FOLLOW_INT_in_synpred6_Imp910 = frozenset([57])
    FOLLOW_57_in_synpred6_Imp912 = frozenset([31])
    FOLLOW_INT_in_synpred6_Imp914 = frozenset([1])
    FOLLOW_57_in_synpred7_Imp939 = frozenset([31])
    FOLLOW_INT_in_synpred7_Imp941 = frozenset([1])
    FOLLOW_ns_ref_in_synpred8_Imp1107 = frozenset([51])
    FOLLOW_51_in_synpred8_Imp1109 = frozenset([1])
    FOLLOW_89_in_synpred9_Imp1135 = frozenset([1])
    FOLLOW_cmp_oper_in_synpred10_Imp1772 = frozenset([76])
    FOLLOW_76_in_synpred10_Imp1774 = frozenset([1])
    FOLLOW_log_oper_in_synpred11_Imp1882 = frozenset([68, 82])
    FOLLOW_log_op_in_synpred11_Imp1884 = frozenset([1])
    FOLLOW_log_expr_in_synpred12_Imp1951 = frozenset([68, 82])
    FOLLOW_log_op_in_synpred12_Imp1953 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from Imp.antlr3.main import ParserMain
    main = ParserMain("ImpLexer", ImpParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
