import unittest

# Discover and run all tests in the 'tests' directory
test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests')

# Run the tests
test_runner = unittest.TextTestRunner()
test_result = test_runner.run(test_suite)

# Check if any tests failed
if test_result.failures or test_result.errors:
    print("Some tests failed.")
else:
    print("All tests passed.")
