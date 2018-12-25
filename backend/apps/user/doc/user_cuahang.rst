==========================
Microservice: User_CuaHang
==========================

Services performed processing CRUD for User_CuaHang

Endpoints
=========

Get user list
    :ref:`GET http://127.0.0.1:8000/user/user/ <get_user_list>`

Create a new user_cuahang
    :ref:`POST http://127.0.0.1:8000/user/user_cuahang/ <post_user_cuahang>`

Get a user_cuahang
    :ref:`GET http://127.0.0.1:8000/user/user_cuahang/{id}/ <get_user_cuahang>`

Update a user_cuahang
    :ref:`PUT http://127.0.0.1:8000/user/user_cuahang/{id}/ <put_user_cuahang>`

Delete a user_cuahang
    :ref:`DELETE http://127.0.0.1:8000/user/user_cuahang/{id}/ <delete_user_cuahang>`


.. _get_user_cuahang_list:

Get user_cuahang list
=====================

GET http://127.0.0.1:8000/user/user_cuahang/

.. _get_user_cuahang_list_request:

Request
-------

::

    # Get 5 user_cuahang and sort by latest added-date
    http://127.0.0.1:8000/user/user_cuahang/?limit=5&sort=latest-added

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

.. _get_user_cuahang_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/user/user_cuahang/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/user/user_cuahang/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "user_id": 1,
                "sanpham_id": 2,
                "tencuahang": "Đệ Nhất Quán 123"
            },
            {
                "id": 2,
                "user_id": 5,
                "sanpham_id": 2,
                "tencuahang": "Đệ Nhất Quán 356"
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
      - http://127.0.0.1:8000/user/user_cuahang/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/user/user_cuahang/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of User_CuaHang <results_response>`


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
      - Id of User_CuaHang

    * - user_id
      - integer
      - 1
      - User_Id of User

    * - sanpham_id
      - integer
      - 2
      - SanPham_Id of SanPham

    * - tencuahang
      - string
      - Đệ Nhất Quán 123
      - TenCuaHang of User_CuaHang

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


.. _post_user_cuahang:

Create a new user_cuahang
=========================

POST http://127.0.0.1:8000/user/user_cuahang/

Request
-------

::

    POST http://127.0.0.1:8000/user/user_cuahang/

    {
        "taikhoan_id": 1,
        "user_id": 1,
        "sanpham_id": 2,
        "tencuahang": "Đệ Nhất Quán 123"
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

    * - user_id
      - True
      - JSON
      - integer
      -
      - 1
      - User_Id of User

    * - sanpham_id
      - True
      - JSON
      - integer
      -
      - 2
      - SanPham_Id of SanPham

    * - tencuahang
      - True
      - JSON
      - string
      -
      - Đệ Nhất Quán 123
      - TenCuaHang of User_CuaHang

.. _user_cuahang_response:

Response
--------

::

    {
        "id": 1,
        "user_id": 1,
        "sanpham_id": 2,
        "tencuahang": "Đệ Nhất Quán 123"
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
      - Id of User_CuaHang

    * - user_id
      - integer
      - 1
      - User_Id of User

    * - sanpham_id
      - integer
      - 2
      - SanPham_Id of SanPham

    * - tencuahang
      - string
      - Đệ Nhất Quán 123
      - TenCuaHang of User_CuaHang

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


.. _get_user_cuahang:

Get a user_cuahang
==================

GET http://127.0.0.1:8000/user/user_cuahang/{id}/

.. _get_user_cuahang_request:

Request
-------

::

    # Get a user_cuahang
    http://127.0.0.1:8000/user/user_cuahang/1/

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
      - ID of User_CuaHang

Response
--------

::

    {
        "id": 1,
        "user_id": 1,
        "sanpham_id": 2,
        "tencuahang": "Đệ Nhất Quán 123"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User_CuaHang response <user_cuahang_response>`


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


.. _put_user_cuahang:

Update a user_cuahang
=====================

PUT http://127.0.0.1:8000/user/user_cuahang/{id}/

.. _put_user_cuahang_request:

Request
-------

::

    # Update a user_cuahang
    PUT http://127.0.0.1:8000/user/user_cuahang/1/

    {
        "user_id": 10,
        "sanpham_id": 1,
        "tencuahang": "Đệ Nhất Quán"
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
      - Id of User_CuaHang

    * - user_id
      - True
      - Query string
      - integer
      -
      - 10
      - New user_id of User

    * - sanpham_id
      - True
      - Query string
      - integer
      -
      - 1
      - New sanpham_id of SanPham

    * - tensanpham
      - True
      - Query string
      - string
      -
      - Đệ Nhất Quán
      - New tensanpham of User_CuaHang

Response
--------

::

    {
        "id": 1,
        "user_id": 10,
        "sanpham_id": 1,
        "tencuahang": "Đệ Nhất Quán"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST User_CuaHang response <user_cuahang_response>`


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

.. _delete_user_cuahang:

Delete a user_cuahang
=====================

DELETE http://127.0.0.1:8000/user/user_cuahang/{id}/

Request
-------

::

    # Delete a user_cuahang
    DELETE http://127.0.0.1:8000/user/user_cuahang/1/

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
      - ID of User_CuaHang

.. _delete_user_cuahang_response:

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
