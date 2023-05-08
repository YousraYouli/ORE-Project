
import re

class Md_to_html(): # converts md content to Html
    def __init__(self,content):
        self.content = content
    def convert(self):
        self.convert_blockquote()
        self.convert_links()
        self.convert_headers()
        self.convert_bold()
        self.convert_italic()
        self.convert_ul()
        self.convert_ol()
        self.convert_imgs()
        self.convert_code()
        return self.content

    def convert_headers(self):
        patt = re.compile("(#+ .+\\n)")
        resu = patt.findall(self.content)
        for res in resu:
            splitted = res.split(" ")
            astroids = splitted[0].strip()
            cntnt = ' '.join(splitted[1:])
            self.content = patt.sub(f'<h{len(astroids)}>{cntnt}</h{len(astroids)}>\n',self.content,1)
                
    def convert_imgs(self):
        patt =  re.compile("!\[([^\[]+)\]\(([^\(]+)\)")
        for res in patt.finditer(self.content):
            result = f'<img src="{res.group(2)}" alt="{res.group(1)}"/>'
            self.content = patt.sub(result,self.content,1) 
            
    def convert_bold(self):
        patt = re.compile("\*\*([^(?:\*\*)\\n]+)\*\*")
        patt2 = re.compile("__([^(?:__)\\n]+)__")
        for res in patt.finditer(self.content):
            result = f'<strong>{res.group(1)}</strong>'
            
            self.content = patt.sub(result,self.content,1)
        for res in patt2.finditer(self.content):
            result = f'<strong>{res.group(1)}</strong>'
            self.content = patt2.sub(result,self.content,1)
    
    def convert_italic(self):
        patt = re.compile("([^\*])\*([^\*\\n]+)\*([^\*])")
        patt2 = re.compile("([^_])_([^_\\n]+)_([^_])")
        for res in patt.finditer(self.content):
            ptt = re.compile("\s+")
            if ptt.match(res.group(2)):
                continue
            result = f'{res.group(1)}<em>{res.group(2)}</em>{res.group(3)}'
            self.content = patt.sub(result,self.content,1)
        for res in patt2.finditer(self.content):
            result = f'{res.group(1)}<em>{res.group(2)}</em>{res.group(3)}'
            self.content = patt2.sub(result,self.content,1)
                  
    def convert_links(self) :
        
        patt = re.compile("([^!])\[([^\[]+)\]\(([^\(]+)\)")
        for res in patt.finditer(self.content):
            result = f'{res.group(1)}<a href="{res.group(3)}">{res.group(2)}</a>'
            self.content = patt.sub(result,self.content,1) 
        
    def convert_ul(self): #unordered list , this will not convert nested lists
        patt = re.compile("[\*-] (.+)\\n")
        self.content = patt.sub("<ul>\\n<li>\\1</li></ul>\\n",self.content)
        self.content = re.sub("</ul>\\n<ul>",'',self.content)

    def convert_ol(self): #ordered list , this will not convert nested lists
        patt = re.compile("\d+\. (.+)\\n")
        self.content = patt.sub("<ol>\\n<li>\\1</li></ol>\\n",self.content)
        self.content = re.sub("</ol>\\n<ol>",'',self.content)
        
    def convert_code(self):
        patt = re.compile("```([^(?:```)]+)```")
        self.content = patt.sub("<code>\\1</code>",self.content)
        patt = re.compile("`([^`]+)`")
        self.content = patt.sub("<code>\\1</code>",self.content)

    def convert_blockquote(self):
        patt = re.compile(">(.+)\\n")
        self.content = patt.sub("<blockquote>\\1</blockquote>\\n",self.content)
        self.content = re.sub("</blockquote>\\n<blockquote>",'\n',self.content)