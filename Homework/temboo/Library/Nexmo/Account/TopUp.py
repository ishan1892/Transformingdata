# -*- coding: utf-8 -*-

###############################################################################
#
# TopUp
# Allows you to top-up your account provided that you've set up "auto-reload" in your Account Settings.
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

class TopUp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopUp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TopUp, self).__init__(temboo_session, '/Library/Nexmo/Account/TopUp')


    def new_input_set(self):
        return TopUpInputSet()

    def _make_result_set(self, result, path):
        return TopUpResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopUpChoreographyExecution(session, exec_id, path)

class TopUpInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopUp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(TopUpInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(TopUpInputSet, self)._set_input('APISecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(TopUpInputSet, self)._set_input('ResponseFormat', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((required, string) The transaction id associated with your **first** 'auto reload' top-up.)
        """
        super(TopUpInputSet, self)._set_input('TransactionID', value)

class TopUpResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopUp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Nexmo. A 200 is returned for a successful request.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. For a successful request, an empty response body is returned.)
        """
        return self._output.get('Response', None)

class TopUpChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopUpResultSet(response, path)
