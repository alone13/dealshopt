=====================
Microservice: DanhMuc
=====================

Services performed processing CRUD for TaiKhoan

Endpoints
=========

Get danhmuc list
    :ref:`GET http://127.0.0.1:8000/danhmuc/danhmuc/ <get_danhmuc_list>`

Create a new danhmuc
    :ref:`POST http://127.0.0.1:8000/danhmuc/danhmuc/ <post_danhmuc>`

Get a danhmuc
    :ref:`GET http://127.0.0.1:8000/danhmuc/danhmuc/{id}/ <get_danhmuc>`

Update a danhmuc
    :ref:`PUT http://127.0.0.1:8000/danhmuc/danhmuc/{id}/ <put_danhmuc>`

Delete a danhmuc
    :ref:`DELETE http://127.0.0.1:8000/danhmuc/danhmuc/{id}/ <delete_danhmuc>`


.. _get_danhmuc_list:

Get danhmuc list
================

GET http://127.0.0.1:8000/danhmuc/danhmuc/

.. _get_danhmuc_list_request:

Request
-------

::

    # Get 5 danhmuc and sort by latest added-date
    http://127.0.0.1:8000/danhmuc/danhmuc/?limit=5&sort=latest-added

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

.. _get_danhmuc_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/danhmuc/danhmuc/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/danhmuc/danhmuc/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "danhmuccha": 0,
                "tendanhmuc": "Món Chay",
                "link": "/danhmuc/monchay/,
                "trangthai": "True"
            },
            {
                "id": 2,
                "danhmuccha": 0,
                "tendanhmuc": "Trái Cây Sạch",
                "link": "/danhmuc/traicay/",
                "trangthai": "True"
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
      - http://127.0.0.1:8000/danhmuc/danhmuc/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/danhmuc/danhmuc/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of DanhMuc <results_response>`


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
      - Id of DanhMuc

    * - danhmuccha
      - integer
      - 0
      - DanhMucCha of DanhMuc

    * - tendanhmuc
      - string
      - Món Chay
      - TenDanhMuc of DanhMuc

    * - link
      - string
      - /danhmuc/monchay/
      - Link of DanhMuc

    * - trangthai
      - boolean
      - True
      - TrangThai of DanhMuc

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


.. _post_danhmuc:

Create a new danhmuc
====================

POST http://127.0.0.1:8000/danhmuc/danhmuc/

Request
-------

::

    POST http://127.0.0.1:8000/danhmuc/danhmuc/

    {
        "danhmuccha": 0,
        "tendanhmuc": "Món Chay",
        "link": "/danhmuc/monchay/",
        "trangthai": "True"
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

    * - danhmuccha
      - True
      - JSON
      - integer
      -
      - 0
      - DanhMucCha of DanhMuc

    * - tendanhmuc
      - True
      - JSON
      - string
      -
      - Món Chay
      - TenDanhMuc of DanhMuc

    * - link
      - True
      - JSON
      - string
      -
      - /danhmuc/monchay/
      - Link of DanhMuc

    * - trangthai
      - True
      - JSON
      - boolean
      -
      - True
      - TrangThai of DanhMuc

.. _danhmuc_response:

Response
--------

::

    {
        "id": 1,
        "danhmuccha": 0,
        "tendanhmuc": "Món Chay",
        "link": "/danhmuc/monchay/",
        "trangthai": "True"
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
      - Id of DanhMuc

    * - danhmuccha
      - integer
      - 0
      - DanhMucCha of DanhMuc

    * - tendanhmuc
      - string
      - Món Chay
      - TenDanhMuc of DanhMuc

    * - link
      - string
      - /danhmuc/monchay/
      - Link of DanhMuc

    * - trangthai
      - boolean
      - True
      - TrangThai of DanhMuc

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


.. _get_danhmuc:

Get a danhmuc
=============

GET http://127.0.0.1:8000/danhmuc/danhmuc/{id}/

.. _get_danhmuc_request:

Request
-------

::

    # Get a danhmuc
    http://127.0.0.1:8000/danhmuc/danhmuc/1/

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
      - ID of DanhMuc

Response
--------

::

    {
        "id": 1,
        "danhmucha": 0,
        "tendanhmuc": "Món Chay",
        "link": "/danhmuc/monchay",
        "trangthai": "True"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST DanhMuc response <danhmuc_response>`


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


.. _put_danhmuc:

Update a danhmuc
================

PUT http://127.0.0.1:8000/danhmuc/danhmuc/{id}/

.. _put_danhmuc_request:

Request
-------

::

    # Update a danhmuc
    PUT http://127.0.0.1:8000/danhmuc/danhmuc/1/

    {
        "danhmuccha": 1,
        "tendanhmuc": "Món Chay",
        "link": "/monchay/",
        "trangthai: "False"
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
      - Id of DanhMuc

    * - danhmuccha
      - True
      - Query string
      - integer
      -
      - 1
      - New danhmuccha of DanhMuc

    * - tendanhmuc
      - True
      - JSON
      - string
      -
      - Món Chay
      - New tendanhmuc of DanhMuc

    * - link
      - True
      - Query string
      - string
      -
      - /monchay/
      - New link of DanhMuc

    * - trangthai
      - True
      - Query string
      - boolean
      -
      - False
      - New trangthai of DanhMuc

Response
--------

::

    {
        "id": 1,
        "danhmuccha": 1,
        "tendanhmuc": "Món Chay",
        "link": "/monchay/",
        "trangthai: "False"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST DanhMuc response <danhmuc_response>`


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

.. _delete_danhmuc:

Delete a danhmuc
================

DELETE http://127.0.0.1:8000/danhmuc/danhmuc/{id}/

Request
-------

::

    # Delete a danhmuc
    DELETE http://127.0.0.1:8000/danhmuc/danhmuc/1/

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
      - ID of DanhMuc

.. _delete_danhmuc_response:

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
