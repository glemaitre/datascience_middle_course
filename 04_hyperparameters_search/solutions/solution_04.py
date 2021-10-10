search_results["mean_score"] = search_results["score"].apply(lambda x: x.mean())
search_results["std_score"] = search_results["score"].apply(lambda x: x.std())
