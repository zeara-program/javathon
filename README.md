# javathon
javathon(ジャヴァソン)はjavascriptをpythonで実行するというパッケージです
# installの方法
```pip install git+https://github.com/zeara-program/javathon/```
# code
```
import javathon
from javathon import console
from javathon import net

# console
#########################
console.log("メッセージ")
#########################

# net
################################################################################
net.get("https://pzearadiscord.000webhostapp.com")# headersを指定しても使えます
data = {
  "name": "zearadisscord",
  "content": "zearadiscordpost"
}
net.post("URL",data=data)
net.delete("URL")# header...(以下略)
################################################################################
```
