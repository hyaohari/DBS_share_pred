#!/usr/bin/env python
# coding: utf-8

# In[36]:


from flask import Flask


# In[37]:


app = Flask(__name__)


# In[38]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS")
        pred = model.predict([[float(rates)]])
        print(pred)
        p="Predicted DBS share price = "+str(pred[0][0])
        print(p)
        return(render_template("index.html", result=p))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




