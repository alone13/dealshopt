====================
Microservice: Module
====================

Services performed processing CRUD for Module

Endpoints
=========

Get module list
    :ref:`GET http://localhost/admin/module/ <get_module_list>`

Create a new module
    :ref:`POST http://localhost/admin/module/ <post_module>`

Get a module
    :ref:`GET http://localhost/admin/module/{id}/ <get_module>`

Update a module
    :ref:`PUT http://localhost/admin/module/{id}/ <put_module>`

Delete a module
    :ref:`DELETE http://localhost/admin/module/{id}/ <delete_module>`


.. _get_module_list:

Get module list
===============

GET http://localhost/admin/module/

.. _get_module_list_request:

Request
-------

::

    # Get 5 module and sort by latest added-date
    http://localhost/admin/module/?limit=5&sort=latest-added

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

.. _get_module_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://localhost/admin/module/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://localhost/admin/module/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "ten": "Module 1"
            },
            {
                "id": 2,
                "ten": "Module 2"
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
      - http://localhost/admin/module/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://localhost/admin/module/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of Module <results_response>`


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
      - Id of Module

    * - ten
      - string
      - Module 1
      - Ten of Module

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


.. _post_module:

Create a new module
===================

POST http://localhost/admin/module/

Request
-------

::

    POST http://localhost/admin/module/

    {
        "ten": "Module 1"
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

    * - ten
      - True
      - JSON
      - string
      -
      - Module 1
      - Ten of Module

.. _module_response:

Response
--------

::

    {
        "id": 1,
        "ten": "Module 1"
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
      - Id of Module

    * - ten
      - string
      - Module 1
      - Ten of Module

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


.. _get_module:

Get a module
============

GET http://localhost/admin/module/{id}/

.. _get_module_request:

Request
-------

::

    # Get a module
    http://localhost/admin/module/1/

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
      - ID of Module

Response
--------

::

    {
        "id": 1,
        "ten": "Module 1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Module response <module_response>`


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


.. _put_module:

Update a module
===============

PUT http://localhost/admin/module/{id}/

.. _put_module_request:

Request
-------

::

    # Update a module
    PUT http://localhost/admin/module/1/

    {
        "ten": "Module update"
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
      - ID of Module

    * - ten
      -
      - JSON
      - string
      -
      - Module update
      - New ten of Module

Response
--------

::

    {
        "id": 1,
        "ten": "Module update"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Module response <module_response>`


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

.. _delete_module:

Delete a module
===============

DELETE http://localhost/admin/module/{id}/

Request
-------

::

    # Delete a module
    DELETE http://localhost/admin/module/1/

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
      - ID of Module

.. _delete_module_response:

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
