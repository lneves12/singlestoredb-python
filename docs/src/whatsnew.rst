
What's New
==========

This document outlines features and improvements from each release.

.. note:: All releases before v1.0.0 are considered pre-release and
   are for non-production testing and evaluation, and may include
   changes to the API.

v0.10.2 - December 14, 2023
---------------------------
* Make workspace group optional in Fusion SQL if it is specified in the environment

v0.10.1 - December 13, 2023
---------------------------
* Cache regions in Management API
* Add dummy fields to Region objects if the region ID does not point to an existing region

v0.10.0 - December 12, 2023
---------------------------
* Add JWT authentication support to Fusion
* Add experimental vector data format support to UDF server
* Rename ``stages`` to ``stage``
* Add ``track_env`` connection parameter to automatically track the ``SINGLESTOREDB_URL``
  environment variable

v0.9.6 - November 2, 2023
-------------------------
* Fusion fixes and testing

v0.9.5 - October 31, 2023
-------------------------
* Add defaults for builtin Fusion rules

v0.9.4 - October 31, 2023
-------------------------
* More Fusion enhancements

v0.9.3 - October 25, 2023
-------------------------
* Fusion fixes

v0.9.2 - October 24, 2023
-------------------------
* Experimental Fusion SQL interface

v0.9.1 - October 17, 2023
-------------------------
* Add name / ID indexing to workspace groups / workspaces / regions

v0.9.0 - October 16, 2023
-------------------------
* Add Stage to Management API

v0.8.9 - October 4, 2023
------------------------
* Add debug option for connections

v0.8.8 - September 26, 2023
---------------------------
* Fix error propagation issue in C extension

v0.8.7 - September 19, 2023
---------------------------
* Add `encoding_errors=` parameter to connection

v0.8.6 - August 29, 2023
------------------------
* Fix ``WITH`` statements in HTTP

v0.8.5 - August 29, 2023
------------------------
* Fix ``DESCRIBE`` statements in HTTP

v0.8.4 - August 28, 2023
------------------------
* Fix boolean connection options

v0.8.3 - August 23, 2023
------------------------
* Fix ``%`` escaping in HTTP queries

v0.8.2 - August 10, 2023
------------------------
* Add ``nan_as_null`` and ``inf_as_null`` options for parameter conversion support
* Separate ``structsequences`` and ``namedtuples`` for ``results_type``
* Performance improvements of binary data uploads

v0.8.1 - July 12, 2023
-----------------------
* Add ``create_engine`` function to return SQLAlchemy engine while supporting
  environment variable parameter settings and settings in options

v0.8.0 - July 12, 2023
-----------------------
* ! Python 3.8 is now the minimum required version
* Add parameter conversion routines to HTTP driver

v0.7.1 - June 15, 2023
----------------------
* Add ``connect_timeout`` and ``multi_statements`` options to connection

v0.7.0 - June 9, 2023
---------------------
* Add converters for numpy array to vector blobs,
  and pygeos / shapely objects to geography data

v0.6.1 - May 18, 2023
---------------------
* Fix GSSAPI/Kerberos packet data

v0.6.0 - May 17, 2023
---------------------
* Added GSSAPI/Kerberos support

v0.5.4 - March 15, 2023
-----------------------
* Added expiration to workspaces

v0.5.3 - January 9, 2023
--------------------------
* Fixed issue with parsing numeric results

v0.5.2 - December 14, 2022
--------------------------
* Fixed issues with unbuffered reads

v0.5.1 - December 9, 2022
-------------------------
* Added 32-bit Windows and aarch64 Linux packages
* Added option to log queries

v0.5.0 - December 8, 2022 (**API CHANGES**)
-------------------------------------------
* ! Query parameter syntax has changed from ``:1`` for positional
  and ``:key`` for dictionary keys to ``%s`` for positional and ``%(key)s``
  for dictionary keys
* ! ``results_format`` connection parameter has changed to ``results_type``
* High-performance C extension added
* Added ``ssl_verify_cert`` and ``ssl_verify_identity`` connection options
* Add Python 3.11 support

v0.4.0 - October 19, 2022
-------------------------
* Add Python 3.6 support

v0.3.3 - September 21, 2022
---------------------------
* Add ``ssl_cipher`` option to connections
* Add ``show`` accessor for database ``SHOW`` commands

v0.3.2 - September 14, 2022
---------------------------
* Fixes for PyMySQL compatibility

v0.3.1 - September 9, 2022
--------------------------
* Changed cipher in PyMySQL connection for SingleStoreDB Cloud compatibility

v0.3.0 - September 9, 2022
--------------------------
* Changed autocommit=True by default

v0.2.0 - August 5, 2022
-----------------------
* Changed to pure Python driver
* Add workspace management objects
* Added ``auth.get_jwt`` function for retrieving JWTs

v0.1.0 - May 6, 2022
--------------------
* DB-API compliant connections
* HTTP API support
* Cluster manager interface
