" IMP syntax file
" Filename:     imp.vim
" Language:     IMP configuration moddeling language
" Maintainer:   Bart Vanbrabant <bart.vanbrabant@cs.kuleuven.be>
" URL:
" Last Change:
" Version:
"

if exists("b:current_syntax")
    finish
endif

syn region Comment start="#" end="$"
syn region String start="\"" end="\""
syn region String start="\"\"\"" end="\"\"\""

syn keyword Keyword implementation end using entity when implement extends in or and as matching index
syn keyword Typedef typedef
syn keyword Boolean true false
syn keyword Type string number

"syn match impInstance "\%(\%(def\s\|class\s\|@\)\s*\)\@<=\h\%(\w\|\.\)*" contained

"syntax region Function start="(" end=")"

"highlight link cfComment Comment

let b:current_syntax = "imp"
