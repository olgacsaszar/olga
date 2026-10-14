import datapie as dp

def main(input_data, parameters): # which names should I use here? Are they general names or should I refer to the entry point arguments?
    # I don't know in what format I will get the results. Is it a list?
    db = dp.Databox({"X_1": input_data.get(X_1),
                     "X_2": input_data.get(X_2),
                     "X_3": input_data.get(X_3),
                     "X_4": input_data.get(X_4)})

    start_date = parameters.get(start_date)
    end_date = parameters.get(end_date)

    start_date_q = start_date.refrequent(dp.QUARTERLY)
    end_date_q = end_date.refrequent(dp.QUARTERLY)

    db = db.clip_series(start_date_q, end_date_q)

    Y_1 = db("X_1 * X_2 / 100")
    Y_2 = db("pct(X_3, -4)", series_function_context=True)
    Y_3 = db("X_4")


    output_data = dp.Databox({"Y_1": Y_1,
                              "Y_2": Y_2,
                              "Y_3": Y_3})
    
    return output_data
    