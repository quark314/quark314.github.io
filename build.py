import shutil, os

#shutil.rmtree('./dist')
#shutil.copytree('./', './dist')

t = open('template.tpl.html').read()

for f in os.listdir('./posts'):
     if f.endswith('.tpl.html'):
		f = 'posts/' + f 
		template = t
		print'Compiling', f
		content = open(f)
		title = content.readline()
		template = template.replace('<title></title>', '<title>' + title + '</title>')
		template = template.replace('./styles', '../styles')
		template = template.replace('./photos', '../photos')
		template = template.replace('./index', '../index')
		template = template.replace('<!--BODY GOES HERE-->', content.read())
		compiled = open(f.replace('.tpl', ''), 'w')
		compiled.write(template)
		compiled.close()
        
print 'Compiling index.tpl.html'
content = open('index.tpl.html')
title = content.readline()
t = t.replace('<title></title>', '<title>' + title + '</title>')
t = t.replace('<!--BODY GOES HERE-->', content.read())
compiled = open('index.html', 'w')
compiled.write(t)
compiled.close()
