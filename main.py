from prep import create_data, create_data_test, head_tail, distrib_viz, class_age_viz
from data_cleaning import is_null, missing_values

train = create_data()
test = create_data_test()

head_tail(train, test)
# distrib_viz(train, test)
# class_age_viz(train, test)

is_null(train, test)

missing_values(train, test)



