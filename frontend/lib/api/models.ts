/// <reference path="../../typings/izischool.d.ts"/>

export interface Course {
    id: number;
    name?: string;
}

export interface Role {
    id: number;
    ten: string;
}

export interface Module {
    id: number;
    ten: string;
}

export interface Role_Module {
    id: number;
    module_id?: number;
    role_id?: number;
}

export interface HoatDong {
    id: number;
    ten?: string;
}

export interface Module_HoatDong {
    id: number;
    module_id?: number;
    hoatdong_id?: number;
}

export interface TaiKhoan {
    id: number;
    tendangnhap?: string;
    matkhau?: string;
    role_id?: number;
}

export interface Admin {
    id: number;
    taikhoan_id?: number;
}

export interface User_TrangThai {
    id: number;
    trangthai?: boolean;
}

export interface User {
    id: number;
    taikhoan_id?: number;
    user_trangthai_id?: number;
}

export interface User_CuaHang_SanPham {
    id: number;
    user_id?: number;
    sanpham_id?: number;
    tencuahang?: string;
}

export interface DanhMuc {
    id: number;
    danhmuccha?: number;
    tendanhmuc?: string;
    trangthai?: boolean;
    link?: string;
}

export interface TinhThanh {
    id: number;
    ten?: string;
    trangthai?: boolean;
}

export interface QuanHuyen {
    id: number;
    tinh_id?: number;
    ten?: string;
    trangthai?: boolean;
}

export interface SanPhamBaoMat {
    id: number;
    ten?: string;
}

export interface SanPhamTrangThai {
    id: number;
    trangthai?: boolean;
}

export interface TheLoaiSanPham {
    id: number;
    ten?: string;
    link?: string;
    trangthai?: boolean;
}

export interface AmThuc {
    id: number;
    ten?: string;
    trangthai?: boolean;
}

export interface SanPham {
    id: number;
    user_cuahang_id?: number;
    theloai_id?: number;
    danhmuc_id?: number;
    baomat_id?: number;
    trangthai_id?: number;
    amthuc_id?: number;
    tinhthanh_id?: number;
    quanhuyen_id?: number;
    tensanpham?: string;
    hinhanh?: string;
    ngaydang?: string;
    soluong?: number;
}

export interface LuaChonSanPham {
    id: number;
    sanpham_id?: number;
    ten?: string;
}

export interface SanPhamGia {
    id: number;
    sanpham_id?: number;
}

export interface SanPhamGiaChiTiet {
    id: number;
    sanpham_gia_id?: number;
    gia?: string;
    ngaybd?: string;
    ngaykt?: string;
    is_active?: boolean;

}

export interface KhachHang {
    id: number;
    tenkhachhang?: string;
    diachi?: string;
    email?: string;
    sdt?: number;
}

export interface DonHang {
    id: number;
    khachhang_id?: number;
    ngaydat?: string;
    trangthai?: boolean;
}

export interface ChiTietDonHang {
    id: number;
    donhang_id?: number;
    sanpham_id?: number;
    gia?: string;
    thanhtien?: string;
}

export interface TinTuc {
    id: number;
    danhmuc_id?: number;
    tieude?: string;
    hinhanh?: string;
    mota?: string;
    noidung?: string;
    ngaydang?: string;
    trangthai?: boolean;
}
