# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering, which merges data points based on similarity rather than relying on cluster centroids like k-means, exhibits greater robustness against outliers."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The clustering outcomes of both k-means and agglomerative hierarchical clustering can vary based on factors such as initial conditions and algorithm parameters. Variables such as the number of clusters, initial centroids, choice of distance measure, and linking technique play crucial roles in influencing the final clustering result."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "In specific data scenarios, K-means clustering, despite its speed and memory efficiency compared to agglomerative hierarchical clustering, may not always be the most suitable technique. Alternative clustering algorithms may offer better performance under certain conditions."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting a cluster can either increase or decrease the SSE of the clustering, depending on the choice of the new centroid. As the goal is to minimize the SSE, the decision to split a cluster should be based on the potential improvement in clustering quality."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Lower SSE in k-means clustering, resulting from data points being closer to cluster centers, indicates higher cluster cohesiveness."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In k-means clustering, greater separation between clusters is indicated by higher values of SSB (Between Sum of Squares), reflecting the larger distances between clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means clustering, cohesion and separation are independent measures. Decreasing SSE (cohesion) does not necessarily require an increase in SSB (separation), and vice versa."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "Modifying clusters, adding or removing data points in k-means clustering can lead to changes in both SSE (Within Sum of Squares) and BSS (Between Sum of Squares)."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "In k-means clustering, two separate metrics, separation and cohesion, are used to evaluate cluster quality. Separation measures how distinct a cluster is from its neighbors, while cohesion assesses the closeness of data points within a cluster. These metrics can vary independently depending on the dataset and algorithm used."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "After the k-means algorithm finishes, each shaded circle will contain a single cluster centroid positioned at its center."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "After the k-means algorithm finishes, certain final clusters may contain points from both shaded regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "After the k-means algorithm completes, the final clustering may include an empty cluster."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R^2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a^2+b^2+r^2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*R^2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Optimal clustering will occur."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Given the similar distances between circles A and B and between circles B and C, each centroid is expected to converge within its respective original circle."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "This distribution ensures that each centroid remains closest to the cluster it originated from, contributing to optimal clustering."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The shortest path that separates the top left point in Group A from the top right point in Group B defines their distance."

    # type: set
    answers["(b)"] = {"Group A","Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The longest distance between them is the distance between the bottom left point in Group C and the bottom right point in Group A."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E','B','F','G','C','L','M','I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits the highest entropy, suggesting it contains a diverse mix of land cover types."

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 demonstrates the lowest entropy, indicating a more homogeneous set of land cover categories within it."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Low distances (blue) on the diagonal suggest well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Different colors indicate varied distances between points, implying distinct cluster distributions."
    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Low distances (blue) on the diagonal indicate well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "High distances (other colors) imply clear boundaries between clusters."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Diagonal entries represent distances of points from themselves."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Regions of green and yellow suggest overlapping or less distinct clusters."

    # type: string
    answers["(b) Row 1"] = "Cluster-a"

    # type: string
    answers["(b) Row 2"] = "Cluster-b"

    # type: string
    answers["(b) Row 3"] = "Cluster-c"

    # type: string
    answers["(b) Row 4"] = "Cluster-d"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Row 1 corresponds to Cluster-a, indicating distances between points within this cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 1 corresponds to Cluster-b, indicating distances between points within this cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 1 corresponds to Cluster-c, indicating distances between points within this cluster."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Row 1 corresponds to Cluster-d, indicating distances between points within this cluster."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In this scenario, partitional clustering is suitable as each student belongs to one grade category. The clustering is exclusive as each student is assigned to only one grade category. The classification is complete as it covers all students in the department."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In Figure B, DBSCAN can effectively identify facial representations by analyzing the spatial density of the data points."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "it is a technique that groups together comparable data points to identify patterns within a dataset. Regarding face characteristics l, k-means can be utilized to find patterns within them depending on dimensions, positions, and shapes."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
