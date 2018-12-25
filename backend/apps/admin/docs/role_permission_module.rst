=========================
Microservice: Role_Module
=========================

Services performed processing CRUD for Role_Module

Endpoints
=========

Get permission list
    :ref:`GET http://localhost/admin/permission/ <get_permission_list>`

Create a new permission
    :ref:`POST http://localhost/admin/permission/ <post_permission>`

Get a permission
    :ref:`GET http://localhost/admin/permission/{id}/ <get_permission>`

Update a permission
    :ref:`PUT http://localhost/admin/permission/{id}/ <put_permission>`

Delete a permission
    :ref:`DELETE http://localhost/admin/permission/{id}/ <delete_permission>`


.. _get_permission_list:

Get permission list
===================

GET http://localhost/admin/permission/

.. _get_permission_list_request:

Request
-------

::

    # Get 5 permission and sort by latest added-date
    http://localhost/admin/permission/?limit=5&sort=latest-added

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - limit
      -
      - query string
      - integer
      - 5
      - 5
      - LIMIT number default to be acquired 5

    * - offset
      -
      - query string
      - integer
      - 0
      - 5
      - OFFSET of acquisition number

    * - sort
      -
      - query string
      - string
      - latest-added
      - latest-added
      - Sort by latest added date

.. _get_permission_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://localhost/admin/permission/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://localhost/admin/permission/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "module_id": "1",
                "role_id": "1"
            },
            {
                "id": 2,
                "module_id": "2",
                "role_id": "1"
            },
            ...
        ]
    }

Response Format
^^^^^^^^^^^^^^^

Main
****

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - count
      - integer
      - 5
      - Number of records returned

    * - current
      - url
      - http://localhost/admin/permission/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://localhost/admin/permission/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of Permission <results_response>`


.. _results_response:

results
#######

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - id
      - integer
      - 1
      - Id of Role_Module

    * - module_id
      - integer
      - 1
      - Module_Id of Module

    * - role_id
      - integer
      - 1
      - Role_Id of Role

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR


.. _post_permission:

Create a new permission
=======================

POST http://localhost/admin/permission/

Request
-------

::

    POST http://localhost/admin/permission/

    {
        "module_id": "1",
        "role_id": "1"
    }

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - module_id
      - True
      - JSON
      - integer
      -
      - 1
      - Module_Id of Module

    * - role_id
      - True
      - JSON
      - integer
      -
      - 1
      - Role_Id of Role

.. _permission_response:

Response
--------

::

    {
        "id": 1,
        "module_id": "1",
        "role_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

Main
****

.. list-table::

    * - **name**
      - **data type**
      - **example**
      - **comment**

    * - id
      - integer
      - 1
      - Id of Role_Module

    * - module_id
      - integer
      - 1
      - Module_Id of Module

    * - role_id
      - integer
      - 1
      - Role_Id of Role

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^


.. list-table::

  * - **code**
    - **comment**

  * - 201
    - CREATED

  * - 400
    - BAD REQUEST

  * - 500
    - INTERNAL SERVER ERROR


.. _get_permission:

Get a permission
================

GET http://localhost/admin/permission/{id}/

.. _get_permission_request:

Request
-------

::

    # Get a permission
    http://localhost/admin/permission/1/

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role_Module

Response
--------

::

    {
        "id": 1,
        "module_id": "1",
        "role_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Permission response <permission_response>`


HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR


.. _put_permission:

Update a permission
===================

PUT http://localhost/admin/permission/{id}/

.. _put_permission_request:

Request
-------

::

    # Update a permission
    PUT http://localhost/admin/permission/1/

    {
        "module_id": "2",
        "role_id": "1"
    }

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role_Module

    * - module_id
      -
      - JSON
      - integer
      -
      - 2
      - New module_id of Role_Module

    * - role_id
      -
      - JSON
      - integer
      -
      - 1
      - New role_id of Role_Module

Response
--------

::

    {
        "id": 1,
        "module_id": "2",
        "role_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Permission response <permission_response>`


HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR

.. _delete_permission:

Delete a permission
===================

DELETE http://localhost/admin/permission/{id}/

Request
-------

::

    # Delete a permission
    DELETE http://localhost/admin/permission/1/

Request Format
^^^^^^^^^^^^^^

.. list-table::

    * - **name**
      - **required**
      - **type**
      - **data type**
      - **default**
      - **example**
      - **comment**

    * - id
      - True
      - Query string
      - integer
      -
      - 1
      - ID of Role_Module

.. _delete_permission_response:

Response
--------

::

    Delete method is return status code only.

HTTP Response Status
^^^^^^^^^^^^^^^^^^^^

.. list-table::

  * - **code**
    - **comment**

  * - 200
    - OK

  * - 400
    - BAD REQUEST

  * - 404
    - NOT FOUND

  * - 500
    - INTERNAL SERVER ERROR
