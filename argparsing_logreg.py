import argparse


def my_logistic_regression(penalty , fit_intercept , max_iter , tol):
    from sklearn.linear_model import LogisticRegression
    
    # define a logistic regression object with your input params
    clf = LogisticRegression(penalty=penalty , fit_intercept=
    fit_intercept , max_iter=max_iter , tol=tol)

    return clf


parser = argparse.ArgumentParser(description = 
                                 """You need to specify the following arguments:
                                 1) penalty (there are four options: {'l1', 'l2', 'elasticnet', None}),
                                 2) fit_intercept (dtype: bool),
                                 3) max_iter (dtype: int),
                                 4) tol (dtype: float)""",
                                 epilog = """Documentation is provided at the following link:
                                            https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html""")

parser.add_argument("--penalty", choices = ['l1', 'l2', 'elasticnet', None], help = "type of penalty to be used in model estimation")
parser.add_argument("--fit_intercept", action = "store_true", help = "specifies if a constant should be added to the decision function")
parser.add_argument("--max_iter", default = 100, type = int, help = "maximum number of iterations taken for the solvers to converge")
parser.add_argument("--tol", default = 1e-4, type = float, help = "tolerance for stopping criteria")

args = parser.parse_args()
print(args)
