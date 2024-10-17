from flask import Flask, render_template, request
import networkx as nx
import matplotlib.pyplot as plt
import os
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['number1'])
    num2 = int(request.form['number2'])

    G = nx.Graph()

    G.add_edge(1, 2, weight=0.6)
    G.add_edge(1, 3, weight=0.2)
    G.add_edge(3, 4, weight=0.1)
    G.add_edge(3, 5, weight=0.7)
    G.add_edge(3, 6, weight=0.9)
    G.add_edge(1, 4, weight=0.3)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos=nx.spring_layout(G,seed=7)

    nx.draw_networkx_nodes(G,pos,node_size=700)
    nx.draw_networkx_edges(G,pos,edgelist=elarge,width=6)
    nx.draw_networkx_edges(G,pos,edgelist=esmall,width=6,alpha=0.5,edge_color="b",style="dashed")

    nx.draw_networkx_labels(G,pos,font_size=20,font_family="sans-serif")

    edge_labels=nx.get_edge_attributes(G,"weight")
    nx.draw_networkx_edge_labels(G,pos,edge_labels)

    shortest_path = nx.shortest_path_length(G, source=num1, target=num2, weight='weight')   

    result=f"Shortest path between {num1} and {num2} is {shortest_path}"
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
