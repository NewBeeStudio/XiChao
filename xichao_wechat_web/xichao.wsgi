import sys
sys.path.insert(0,"/home/newbee/git/XiChao/xichao_wechat_web/")
activate_this = '/home/newbee/git/XiChao/xichao_wechat_web/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app.xichao import app as application
