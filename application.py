from flask import Flask, render_template, jsonify, request
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import AjaxDataSource, CustomJS, ColumnDataSource


app = Flask(__name__)

num_votes = 0
votes = 0
uv_lst = [0]
tv_lst = [0]

def make_bokeh_plot():
    plot = figure(plot_height=450, plot_width=900)
    source = ColumnDataSource(data=dict(x=tv_lst, y=uv_lst))
    plot.line('x', 'y', source=source, line_width=4)
    script, div = components(plot)
    return script, div

@app.route("/")
def index():
    scr_bok, div_bok = make_bokeh_plot()
    return render_template("index.html", 
                           scr_bok=scr_bok, 
                           div_bok=div_bok)

@app.route("/up", methods=["POST"])
def upvote():
    global votes
    global num_votes
    votes += 1
    num_votes = tv_lst[-1] + 1
    uv_lst.append(votes)
    tv_lst.append(num_votes)
    scr_bok, div_bok = make_bokeh_plot()
    return render_template("update_content.html", 
                           scr_bok=scr_bok, 
                           div_bok=div_bok)

@app.route("/down", methods=["POST"])
def downvote():
    global votes
    global num_votes 
    num_votes = tv_lst[-1] + 1
    if votes >= 1:
        votes -= 1    
    uv_lst.append(votes)
    tv_lst.append(num_votes)
    scr_bok, div_bok = make_bokeh_plot()
    return render_template("update_content.html", 
                           scr_bok=scr_bok, 
                           div_bok=div_bok)

if __name__ == '__main__':
    app.run(debug=True)
