=============================
Microservice: Module_HoatDong
=============================

Services performed processing CRUD for Module_HoatDong

Endpoints
=========

Get module_hoatdong list
    :ref:`GET http://127.0.0.1:8000/admin/module_hoatdong/ <get_module_hoatdong_list>`

Create a new module_hoatdong
    :ref:`POST http://127.0.0.1:8000/admin/module_hoatdong/ <post_module_hoatdong>`

Get a module_hoatdong
    :ref:`GET http://127.0.0.1:8000/admin/module_hoatdong/{id}/ <get_module_hoatdong>`

Update a module_hoatdong
    :ref:`PUT http://127.0.0.1:8000/admin/module_hoatdong/{id}/ <put_module_hoatdong>`

Delete a module_hoatdong
    :ref:`DELETE http://127.0.0.1:8000/admin/module_hoatdong/{id}/ <delete_module_hoatdong>`


.. _get_module_hoatdong_list:

Get module_hoatdong list
========================

GET http://127.0.0.1:8000/admin/module_hoatdong/

.. _get_module_hoatdong_list_request:

Request
-------

::

    # Get 5 module_hoatdong and sort by latest added-date
    http://127.0.0.1:8000/admin/module_hoatdong/?limit=5&sort=latest-added

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

.. _get_module_hoatdong_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/admin/module_hoatdong/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/admin/module_hoatdong/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "module_id": "1",
                "hoatdong_id": "1"
            },
            {
                "id": 2,
                "module_id": "2",
                "hoatdong_id": "1"
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
      - http://127.0.0.1:8000/admin/module_hoatdong/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/admin/module_hoatdong/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of Module_HoatDong <results_response>`


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
      - Id of Module_HoatDong

    * - module_id
      - integer
      - 1
      - Module_Id of Module

    * - hoatdong_id
      - integer
      - 1
      - HoatDong_Id of HoatDong

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


.. _post_module_hoatdong:

Create a new module_hoatdong
============================

POST http://127.0.0.1:8000/admin/module_hoatdong/

Request
-------

::

    POST http://localhost/admin/module_hoatdong/

    {
        "module_id": "1",
        "hoatdong_id": "1"
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

    * - hoatdong_id
      - True
      - JSON
      - integer
      -
      - 1
      - HoatDong_Id of HoatDong

.. _module_hoatdong_response:

Response
--------

::

    {
        "id": 1,
        "module_id": "1",
        "hoatdong_id": "1"
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
      - Id of Module_HoatDong

    * - module_id
      - integer
      - 1
      - Module_Id of Module

    * - hoatdong_id
      - integer
      - 1
      - HoatDong_Id of HoatDong

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


.. _get_module_hoatdong:

Get a module_hoatdong
=====================

GET http://127.0.0.1:8000/admin/module_hoatdong/{id}/

.. _get_module_hoatdong_request:

Request
-------

::

    # Get a module_hoatdong
    http://127.0.0.1:8000/admin/module_hoatdong/1/

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
      - ID of Module_HoatDong

Response
--------

::

    {
        "id": 1,
        "module_id": "1",
        "hoatdong_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Module_HoatDong response <module_hoatdong_response>`


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


.. _put_module_hoatdong:

Update a module_hoatdong
========================

PUT http://127.0.0.1:8000/admin/module_hoatdong/{id}/

.. _put_module_hoatdong_request:

Request
-------

::

    # Update a module_hoatdong
    PUT http://127.0.0.1:8000/admin/module_hoatdong/1/

    {
        "module_id": "2",
        "hoatdong_id": "1"
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
      - ID of Module_HoatDong

    * - module_id
      -
      - JSON
      - integer
      -
      - 2
      - New module_id of Module_HoatDong

    * - hoatdong_id
      -
      - JSON
      - integer
      -
      - 1
      - New hoatdong_id of Module_HoatDong

Response
--------

::

    {
        "id": 1,
        "module_id": "2",
        "hoatdong_id": "1"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST Module_HoatDong response <module_hoatdong_response>`


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

.. _delete_module_hoatdong:

Delete a module_hoatdong
========================

DELETE http://127.0.0.1:8000/admin/module_hoatdong/{id}/

Request
-------

::

    # Delete a module_hoatdong
    DELETE http://127.0.0.1:8000/admin/module_hoatdong/1/

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
      - ID of Module_HoatDong

.. _delete_module_hoatdong_response:

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
