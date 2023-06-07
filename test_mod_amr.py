import unittest
import mod_amr
from mod_amr import inserting_value
from unittest.mock import patch, MagicMock
import pandas as pd

class test_mod(unittest.TestCase):
    
    @patch('mod_amr.connection')
    def test_insert(self,mock_connection):
        
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_cur.mogrify.return_value = "(1,'A')".encode(encoding = 'UTF-8')
        mock_cur.execute.return_value = None
        
        A = {'col1': [1],
            'col2':['A']}
        B = pd.DataFrame(A)
        
        mock_connection.return_value.__enter__.return_value = (mock_conn,mock_cur)
        
        self.assertEqual(inserting_value(B,'random','table'),"INSERT INTO table VALUES (1,'A')")
        
if __name__ == "__main__":
    unittest.main()
    
# https://flexiple.com/python/python-string-to-bytes/
# https://stackoverflow.com/questions/28850070/python-mocking-a-context-manager
    
# So, this is what I understand from unittest till now - 
# Unit testing is a white box testing technique

# Blackbox Testing : Testing an application without any knowledge of how the internal application works

# Whitebox Testing: Testing an application with knowledge of how the internal works, such as by having the source code side by side while you are doing your test.

# Unit Testing: This is where you create tests which interact directly with your application. You would check a function in your application and assert that the response should return with value X. Unit Tests are usually, but not always created by the developers themselves as well, whereas if a company does whitebox and blackbox testing, it can be done by anyone.


## Integration testing = Testing multiple modules
## System testing - functional and non-function testing
## Regretion testinf - maintaince testing.

# https://www.youtube.com/watch?v=NPp2pvhGbkM

## Properties of unit test
# 1. Each test should be independent
# 2. External sources should be managed by test doubles (MOcks/fakes/stubs).


# AAA model
# Arrage - preparation
# Act - running the function
# Assert - add required output


# Mocks => reflection of external interfaces
# It is not for function behaviour or return type
# WHy mocks are used
# - Right call, no. of calls, calls with right set of parameters


# Stubs 
# Its like side_effect 
# Returns success, failure or exception
# Checks the behaviour of coed under test in case of these return values


# Fakes
# Suppose you thing my function can handle large data so,
# Taking input from localserver than actual server. for data which is maintain by us.







    
        