# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketNotification
# Enables Amazon SNS notifications of specified events for a bucket.
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

class PutBucketNotification(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketNotification Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutBucketNotification, self).__init__(temboo_session, '/Library/Amazon/S3/PutBucketNotification')


    def new_input_set(self):
        return PutBucketNotificationInputSet()

    def _make_result_set(self, result, path):
        return PutBucketNotificationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketNotificationChoreographyExecution(session, exec_id, path)

class PutBucketNotificationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketNotification
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutBucketNotificationInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutBucketNotificationInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create a notification for.)
        """
        super(PutBucketNotificationInputSet, self)._set_input('BucketName', value)
    def set_Event(self, value):
        """
        Set the value of the Event input for this Choreo. ((optional, string) A bucket event for which to send notifications. Valid value:  "s3:ReducedRedundancyLostObject" (The default and currently only supported notification event).)
        """
        super(PutBucketNotificationInputSet, self)._set_input('Event', value)
    def set_Topic(self, value):
        """
        Set the value of the Topic input for this Choreo. ((conditional, string) The Amazon SNS topic arn that  Amazon S3 will publish a message to report the specified events for the bucket. If this is not supplied, notifications will be turned off.)
        """
        super(PutBucketNotificationInputSet, self)._set_input('Topic', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((required, string) The AWS region that corresponds to the S3 endpoint you wish to access. The default region is "us-east-1".)
        """
        super(PutBucketNotificationInputSet, self)._set_input('UserRegion', value)

class PutBucketNotificationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketNotification Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Stores the response from Amazon. Note that for a successful execution, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketNotificationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutBucketNotificationResultSet(response, path)
