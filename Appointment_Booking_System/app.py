import sqlite3
from flask import Flask,request,redirect,render_template_string
app=Flask(__name__); DB="appointments.db"
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
 c.execute("CREATE TABLE IF NOT EXISTS appointments(id INTEGER PRIMARY KEY,name TEXT,reason TEXT,day TEXT,time TEXT)"); c.commit(); return c
HTML="""<!doctype html><meta name=viewport content="width=device-width"><title>Appointment Booking</title><style>body{font:16px Arial;max-width:900px;margin:30px auto;padding:0 15px;background:#fdf2f8}.box{background:white;padding:18px;border-radius:12px;margin:12px 0}h1{color:#be185d}input,button{padding:10px;margin:4px}button{background:#be185d;color:white;border:0;border-radius:5px}table{width:100%;border-collapse:collapse}td,th{padding:9px;border-bottom:1px solid #ddd;text-align:left}</style><h1>📅 Appointment Booking System</h1><div class=box><form method=post action=/add><input name=name placeholder="Full name" required><input name=reason placeholder="Purpose" required><input name=day type=date required><input name=time type=time required><button>Book appointment</button></form></div><div class=box><h3>Upcoming / saved appointments</h3><table><tr><th>Name</th><th>Purpose</th><th>Date</th><th>Time</th><th></th></tr>{% for a in items %}<tr><td>{{a.name}}</td><td>{{a.reason}}</td><td>{{a.day}}</td><td>{{a.time}}</td><td><a href="/cancel/{{a.id}}">Cancel</a></td></tr>{% endfor %}</table></div>"""
@app.get("/")
def home():
 c=db(); xs=c.execute("SELECT * FROM appointments ORDER BY day,time").fetchall(); c.close(); return render_template_string(HTML,items=xs)
@app.post("/add")
def add():
 c=db(); c.execute("INSERT INTO appointments(name,reason,day,time) VALUES(?,?,?,?)",(request.form["name"],request.form["reason"],request.form["day"],request.form["time"])); c.commit(); c.close(); return redirect("/")
@app.get("/cancel/<int:i>")
def cancel(i):
 c=db(); c.execute("DELETE FROM appointments WHERE id=?",(i,)); c.commit(); c.close(); return redirect("/")
if __name__=="__main__": app.run(debug=True)
