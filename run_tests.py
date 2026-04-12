import sys
from tests.test_recommendation import test_extract_user_features, test_score_resource, test_score_all, test_recommend_engine

try:
    test_extract_user_features()
    print("test_extract_user_features passed")
    test_score_resource()
    print("test_score_resource passed")
    test_score_all()
    print("test_score_all passed")
    test_recommend_engine()
    print("test_recommend_engine passed")
    print("ALL TESTS PASSED")
except AssertionError as e:
    print(f"TEST FAILED")
    raise e
