# -*- coding: utf-8 -*-

###############################################################################
#
# ListCommits
# Lists commits for a specified repository.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCommits(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCommits Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListCommits, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Commits/ListCommits')


    def new_input_set(self):
        return ListCommitsInputSet()

    def _make_result_set(self, result, path):
        return ListCommitsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCommitsChoreographyExecution(session, exec_id, path)

class ListCommitsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCommits
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        super(ListCommitsInputSet, self)._set_input('AccessToken', value)
    def set_Author(self, value):
        """
        Set the value of the Author input for this Choreo. ((optional, string) GitHub login or email address by which to filter by commit author.)
        """
        super(ListCommitsInputSet, self)._set_input('Author', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. Defaults to 1.)
        """
        super(ListCommitsInputSet, self)._set_input('Page', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) Returns only commits containing this file path.)
        """
        super(ListCommitsInputSet, self)._set_input('Path', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page.)
        """
        super(ListCommitsInputSet, self)._set_input('PerPage', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repository.)
        """
        super(ListCommitsInputSet, self)._set_input('Repo', value)
    def set_SHA(self, value):
        """
        Set the value of the SHA input for this Choreo. ((optional, string) The SHA or branch to start listing commits from.)
        """
        super(ListCommitsInputSet, self)._set_input('SHA', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) Only commits after this date will be returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.)
        """
        super(ListCommitsInputSet, self)._set_input('Since', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) Only commits before this date will be returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.)
        """
        super(ListCommitsInputSet, self)._set_input('Until', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(ListCommitsInputSet, self)._set_input('User', value)

class ListCommitsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCommits Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_FirstPage(self):
        """
        Retrieve the value for the "FirstPage" output from this Choreo execution. ((integer) The index for the first page of results.)
        """
        return self._output.get('FirstPage', None)
    def get_LastPage(self):
        """
        Retrieve the value for the "LastPage" output from this Choreo execution. ((integer) The index for the last page of results.)
        """
        return self._output.get('LastPage', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) The index for the next page of results.)
        """
        return self._output.get('NextPage', None)
    def get_PreviousPage(self):
        """
        Retrieve the value for the "PreviousPage" output from this Choreo execution. ((integer) The index for the previous page of results.)
        """
        return self._output.get('PreviousPage', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)

class ListCommitsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListCommitsResultSet(response, path)
