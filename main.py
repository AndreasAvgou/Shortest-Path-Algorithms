
import time
import csv
import matplotlib.pyplot as plt
from graph_generator import generate_graph
from graph_algorithms import *

EXPERIMENTS = [
    (10, 50, 25),
    (20, 50, 20),
    (30, 100, 30),
    (40, 100, 25),
    (50, 100, 20),
]

CSV_FILE = "measurements.csv"

def append_to_csv(row):
    header = ["N", "DijMatrix", "DijList", "BFMatrix", "BFList"]
    try:
        open(CSV_FILE).read()
        exists = True
    except:
        exists = False
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerow(row)

def run_experiments():
    results = {"N": [], "DM": [], "DL": [], "BM": [], "BL": []}
    for N, L, R in EXPERIMENTS:
        matrix, adj_list = generate_graph(N, L, R)

        start = time.time()
        for s in range(N):
            dijkstra_matrix(matrix, s)
        t_dm = time.time() - start

        start = time.time()
        for s in range(N):
            dijkstra_list(adj_list, s)
        t_dl = time.time() - start

        start = time.time()
        for s in range(N):
            bellman_ford_matrix(matrix, s)
        t_bm = time.time() - start

        start = time.time()
        for s in range(N):
            bellman_ford_list(adj_list, s)
        t_bl = time.time() - start

        append_to_csv([N, t_dm, t_dl, t_bm, t_bl])

        results["N"].append(N)
        results["DM"].append(t_dm)
        results["DL"].append(t_dl)
        results["BM"].append(t_bm)
        results["BL"].append(t_bl)

    return results

def plot_results(results):
    N = results["N"]
    plt.plot(N, results["DM"], marker="o", label="Dijkstra Matrix")
    plt.plot(N, results["DL"], marker="o", label="Dijkstra List")
    plt.plot(N, results["BM"], marker="o", label="Bellman-Ford Matrix")
    plt.plot(N, results["BL"], marker="o", label="Bellman-Ford List")
    plt.xlabel("N nodes")
    plt.ylabel("Execution time")
    plt.legend()
    plt.grid(True)
    plt.savefig("plot.png")
    plt.show()

if __name__ == "__main__":
    r = run_experiments()
    plot_results(r)
