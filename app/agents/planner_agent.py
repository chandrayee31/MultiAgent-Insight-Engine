def planner_agent(question:str)-> dict:

    plan = {
        'question':question,
        'steps':[
            'load the dataset',
            'analysis of monthly and category of sales trend',
            'the main reason for the change',
            'generate a business friendlt summary'
        ]
    }



    return plan