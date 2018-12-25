======================
Microservice: TaiKhoan
======================

Services performed processing CRUD for TaiKhoan

Endpoints
=========

Get taikhoan list
    :ref:`GET http://127.0.0.1:8000/taikhoan/taikhoan/ <get_taikhoan_list>`

Create a new taikhoan
    :ref:`POST http://127.0.0.1:8000/taikhoan/taikhoan/ <post_taikhoan>`

Get a taikhoan
    :ref:`GET http://127.0.0.1:8000/taikhoan/taikhoan/{id}/ <get_taikhoan>`

Update a taikhoan
    :ref:`PUT http://127.0.0.1:8000/taikhoan/taikhoan/{id}/ <put_taikhoan>`

Delete a taikhoan
    :ref:`DELETE http://127.0.0.1:8000/taikhoan/taikhoan/{id}/ <delete_taikhoan>`


.. _get_taikhoan_list:

Get taikhoan list
=================

GET http://127.0.0.1:8000/taikhoan/taikhoan/

.. _get_taikhoan_list_request:

Request
-------

::

    # Get 5 taikhoan and sort by latest added-date
    http://127.0.0.1:8000/taikhoan/taikhoan/?limit=5&sort=latest-added

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

.. _get_taikhoan_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/taikhoan/taikhoan/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/taikhoan/taikhoan/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "tendangnhap": "ThaoHuong",
                "matkhau": "ThaoHuong",
                "role_id": 1
            },
            {
                "id": 2,
                "tendangnhap": "ThaoHuong11",
                "matkhau": "ThaoHuong11",
                "role_id": 1
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
      - http://127.0.0.1:8000/taikhoan/taikhoan/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/taikhoan/taikhoan/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of TaiKhoan <results_response>`


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
      - Id of TaiKhoan

    * - tendangnhap
      - string
      - ThaoHuong
      - TenDangNhap of TaiKhoan

    * - matkhau
      - string
      - ThaoHuong
      - MatKhau of TaiKhoan

    * - role_id
      - integer
      - 1
      - Role_Id of TaiKhoan

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


.. _post_taikhoan:

Create a new taikhoan
=====================

POST http://127.0.0.1:8000/taikhoan/taikhoan/

Request
-------

::

    POST http://127.0.0.1:8000/taikhoan/taikhoan/

    {
        "tendangnhap": "ThaoHuong",
        "matkhau": "ThaoHuong",
        "role_id": 1
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

    * - tendangnhap
      - True
      - JSON
      - string
      -
      - ThaoHuong
      - TenDangNhap of TaiKhoan

    * - matkhau
      - True
      - JSON
      - string
      -
      - ThaoHuong
      - MatKhau of TaiKhoan

    * - role_id
      - True
      - JSON
      - integer
      -
      - 1
      - Role_Id of TaiKhoan

.. _taikhoan_response:

Response
--------

::

    {
        "id": 1,
        "tendangnhap": "ThaoHuong",
        "matkhau": "ThaoHuong",
        "role_id": 1
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
      - Id of TaiKhoan

    * - tendangnhap
      - string
      - ThaoHuong
      - TenDangNhap of TaiKhoan

    * - matkhau
      - string
      - ThaoHuong
      - MatKhau of TaiKhoan

    * - role_id
      - integer
      - 1
      - Role_Id of TaiKhoan

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


.. _get_taikhoan:

Get a taikhoan
==============

GET http://127.0.0.1:8000/taikhoan/taikhoan/{id}/

.. _get_taikhoan_request:

Request
-------

::

    # Get a taikhoan
    http://127.0.0.1:8000/taikhoan/taikhoan/1/

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
      - ID of TaiKhoan

Response
--------

::

    {
        "id": 1,
        "tendangnhap": "ThaoHuong",
        "matkhau": "ThaoHuong",
        "role_id": 1
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST TaiKhoan response <taikhoan_response>`


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


.. _put_taikhoan:

Update a taikhoan
=================

PUT http://127.0.0.1:8000/taikhoan/taikhoan/{id}/

.. _put_taikhoan_request:

Request
-------

::

    # Update a taikhoan
    PUT http://127.0.0.1:8000/taikhoan/taikhoan/1/

    {
        "tendangnhap": "ThaoHuong1995",
        "matkhau": "ThaoHuong1995",
        "role_id": 2
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
      - Id of TaiKhoan

    * - tendangnhap
      - True
      - Query string
      - string
      -
      - ThaoHuong1995
      - New tendangnhap of TaiKhoan

    * - matkhau
      - True
      - JSON
      - string
      -
      - ThaoHuong1995
      - New matkhau of TaiKhoan

    * - role_id
      - True
      - Query string
      - integer
      -
      - 2
      - New role_id of TaiKhoan

Response
--------

::

    {
        "id": 1,
        "tendangnhap": "ThaoHuong1995",
        "matkhau": "ThaoHuong1995",
        "role_id": 2
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST TaiKhoan response <taikhoan_response>`


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

.. _delete_taikhoan:

Delete a taikhoan
=================

DELETE http://127.0.0.1:8000/taikhoan/taikhoan/{id}/

Request
-------

::

    # Delete a taikhoan
    DELETE http://127.0.0.1:8000/taikhoan/taikhoan/1/

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
      - ID of TaiKhoan

.. _delete_taikhoan_response:

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
