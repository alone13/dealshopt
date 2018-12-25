====================
Microservice: TinTuc
====================

Services performed processing CRUD for TinTuc

Endpoints
=========

Get tintuc list
    :ref:`GET http://127.0.0.1:8000/tintuc/tintuc/ <get_tintuc_list>`

Create a new tintuc
    :ref:`POST http://127.0.0.1:8000/tintuc/tintuc/ <post_tintuc>`

Get a tintuc
    :ref:`GET http://127.0.0.1:8000/tintuc/tintuc/{id}/ <get_tintuc>`

Update a tintuc
    :ref:`PUT http://127.0.0.1:8000/tintuc/tintuc/{id}/ <put_tintuc>`

Delete a tintuc
    :ref:`DELETE http://127.0.0.1:8000/tintuc/tintuc/{id}/ <delete_tintuc>`


.. _get_tintuc_list:

Get tintuc list
===============

GET http://127.0.0.1:8000/tintuc/tintuc/

.. _get_tintuc_list_request:

Request
-------

::

    # Get 5 tintuc and sort by latest added-date
    http://127.0.0.1:8000/tintuc/tintuc/?limit=5&sort=latest-added

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

.. _get_tintuc_list_response:

Response
--------

::

    {
        "count": 5,
        "current": "http://127.0.0.1:8000/tintuc/tintuc/?limit=5&offset=0&sort=latest-added",
        "prev": null,
        "next": "http://127.0.0.1:8000/tintuc/tintuc/?limit=5&offset=5&sort=latest-added",
        "results": [
            {
                "id": 1,
                "danhmuc_id": 11,
                "tieude": "Dạy Nấu Ăn",
                "hinhanh": "nauan.jpg,
                "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
                "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
                "ngaydang": "1/1/2016",
                "trangthai": "True"
            },
            {
                "id": 2,
                "danhmuc_id": 1,
                "tieude": "Tin Hàng Ngày",
                "hinhanh": "nauan1.jpg,
                "mota": "Bí quyết nhỏ cho các bạn mê nấu nướng",
                "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
                "ngaydang": "1/3/2016",
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
      - http://127.0.0.1:8000/tintuc/tintuc/?limit=5&offset=0&sort=latest-added
      - Current page

    * - prev
      - url
      - null
      - Previous page

    * - next
      - url
      - http://127.0.0.1:8000/tintuc/tintuc/?limit=5&offset=5&sort=latest-added
      - Next page

    * - results
      - array
      - []
      - :ref:`Records of TinTuc <results_response>`


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
      - Id of TinTuc

    * - danhmuc_id
      - integer
      - 11
      - DanhMuc_Id of DanhMuc

    * - tieude
      - string
      - Dạy Nấu Ăn
      - Tiêu Đề of Tintuc

    * - hinhanh
      - string
      - nauan.jpg
      - HinhAnh of TinTuc

    * - mota
      - string
      - Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh
      - MoTa of TinTuc

    * - noidung
      - string
      - Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...
      - NoiDung of TinTuc

    * - ngaydang
      - date
      - 1/1/2016
      - NgayDang of TinTuc

    * - trangthai
      - boolean
      - True
      - TrangThai of TinTuc

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


.. _post_tintuc:

Create a new tintuc
===================

POST http://127.0.0.1:8000/tintuc/tintuc/

Request
-------

::

    POST http://127.0.0.1:8000/tintuc/tintuc/

    {
        "danhmuc_id": 11,
        "tieude": "Dạy Nấu Ăn",
        "hinhanh": "nauan.jpg,
        "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
        "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
        "ngaydang": "1/1/2016",
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

    * - danhmuc_id
      - True
      - JSON
      - integer
      -
      - 0
      - DanhMuc_Id of DanhMuc

    * - tieude
      - True
      - JSON
      - string
      -
      - Dạy Nấu Ăn
      - TieuDe of TinTuc

    * - hinhanh
      - True
      - JSON
      - string
      -
      - nauan.jpg
      - HinhAnh of TinTuc

    * - mota
      - True
      - JSON
      - string
      -
      - Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh
      - MoTa of TinTuc

    * - noidung
      - True
      - JSON
      - string
      -
      - Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...
      - NoiDung of TinTuc

    * - ngaydang
      - True
      - JSON
      - date
      -
      - 1/1/2016
      - NgayDang of TinTuc

    * - trangthai
      - True
      - JSON
      - boolean
      -
      - True
      - TrangThai of DanhMuc

.. _tintuc_response:

Response
--------

::

    {
        "id": 1,
        "danhmuc_id": 11,
        "tieude": "Dạy Nấu Ăn",
        "hinhanh": "nauan.jpg,
        "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
        "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
        "ngaydang": "1/1/2016",
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
      - Id of TinTuc

    * - danhmuc_id
      - integer
      - 11
      - DanhMuc_Id of DanhMuc

    * - tieude
      - string
      - Dạy Nấu Ăn
      - TieuDe of TinTuc

    * - hinhanh
      - string
      - nauan.jpg
      - HinhAnh of TinTuc

    * - mota
      - string
      - Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh
      - MoTa of TinTuc

    * - noidung
      - string
      - Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...
      - NoiDung of TinTuc

    * - ngaydang
      - date
      - 1/1/2016
      - NgayDang of TinTuc

    * - trangthai
      - boolean
      - True
      - TrangThai of TinTuc

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


.. _get_tintuc:

Get a tintuc
============

GET http://127.0.0.1:8000/tintuc/tintuc/{id}/

.. _get_tintuc_request:

Request
-------

::

    # Get a tintuc
    http://127.0.0.1:8000/tintuc/tintuc/1/

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
      - ID of TinTuc

Response
--------

::

    {
        "id": 1,
        "danhmuc_id": 11,
        "tieude": "Dạy Nấu Ăn",
        "hinhanh": "nauan.jpg,
        "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
        "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
        "ngaydang": "1/1/2016",
        "trangthai": "True"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST TinTuc response <tintuc_response>`


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


.. _put_tintuc:

Update a tintuc
===============

PUT http://127.0.0.1:8000/tintuc/tintuc/{id}/

.. _put_tintuc_request:

Request
-------

::

    # Update a tintuc
    PUT http://127.0.0.1:8000/tintuc/tintuc/1/

    {
        "danhmuc_id": 10,
        "tieude": "Tiêu Đề Update",
        "hinhanh": "nauan.jpg,
        "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
        "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
        "ngaydang": "1/1/2016",
        "trangthai": "False"
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
      - Id of TinTuc

    * - danhmuc_id
      - True
      - Query string
      - integer
      -
      - 10
      - New danhmuc_Id of DanhMuc

    * - tieude
      -
      - JSON
      - string
      -
      - Tiêu Đề Update
      - New tieude of Tintuc

    * - hinhanh
      - True
      - Query string
      - string
      -
      - nauan.jpg
      - New hinhanh of TinTuc

    * - mota
      - True
      - Query string
      - string
      -
      - Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh
      - New mota of TinTuc

    * - noidung
      - True
      - Query string
      - string
      -
      - Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...
      - New noidung of TinTuc

    * - ngaydang
      - True
      - Query string
      - date
      -
      - 1/1/2016
      - New ngaydang of TinTuc

    * - trangthai
      - True
      - Query string
      - boolean
      -
      - False
      - New trangthai of TinTuc

Response
--------

::

    {
        "id": 1,
       "danhmuc_id": 10,
        "tieude": "Tiêu Đề Update",
        "hinhanh": "nauan.jpg,
        "mota": "Bí quyết nhỏ cho các bạn nấu các món hầm thật nhanh",
        "noidung": "Phần lớn các bạn ngày nay đều phải đi làm, thời gian chuẩn bị...",
        "ngaydang": "1/1/2016",
        "trangthai": "False"
    }

Response Format
^^^^^^^^^^^^^^^

:ref:`Same as POST TinTuc response <tintuc_response>`


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

.. _delete_tintuc:

Delete a tintuc
===============

DELETE http://127.0.0.1:8000/tintuc/tintuc/{id}/

Request
-------

::

    # Delete a tintuc
    DELETE http://127.0.0.1:8000/tintuc/tintuc/1/

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
      - ID of TinTuc

.. _delete_tintuc_response:

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
