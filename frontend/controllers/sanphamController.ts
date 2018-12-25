/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ISanPhamPageLogic } from "../pagelogics/sanphamPageLogic";
import { IDanhMucPageLogic } from "../pagelogics/danhmucPageLogic";
import { ITheLoaiSanPhamPageLogic } from "../pagelogics/theloaisanphamPageLogic";
import { ISanPhamBaoMatPageLogic } from "../pagelogics/sanphambaomatPageLogic";
import { ISanPhamTrangThaiPageLogic } from "../pagelogics/sanphamtrangthaiPageLogic";
import { IAmThucPageLogic } from "../pagelogics/amthucPageLogic";
import { ITinhThanhPageLogic } from "../pagelogics/tinhthanhPageLogic";
import { IQuanHuyenPageLogic } from "../pagelogics/quanhuyenPageLogic";
import { sanphamForm } from "../forms/sanphamForms";

export class SanPhamController extends Controller {
    static $inject: string[] = ["SanPhamPageLogic", "DanhMucPageLogic", "TheLoaiSanPhamPageLogic", "SanPhamBaoMatPageLogic", "SanPhamTrangThaiPageLogic", "AmThucPageLogic", "TinhThanhPageLogic", "QuanHuyenPageLogic"];

    private sanphamPageLogic: ISanPhamPageLogic;
    private danhmucPageLogic: IDanhMucPageLogic;
    private theloaiPageLogic: ITheLoaiSanPhamPageLogic;
    private baomatPageLogic: ISanPhamBaoMatPageLogic;
    private trangthaiPageLogic: ISanPhamTrangThaiPageLogic;
    private amthucPageLogic: IAmThucPageLogic;
    private tinhthanhPageLogic: ITinhThanhPageLogic;
    private quanhuyenPageLogic: IQuanHuyenPageLogic;

    constructor(
        sanphamPageLogic: ISanPhamPageLogic,
        danhmucPageLogic: IDanhMucPageLogic,
        theloaiPageLogic: ITheLoaiSanPhamPageLogic,
        baomatPageLogic: ISanPhamBaoMatPageLogic,
        trangthaiPageLogic: ISanPhamTrangThaiPageLogic,
        amthucPageLogic: IAmThucPageLogic,
        tinhthanhPageLogic: ITinhThanhPageLogic,
        quanhuyenPageLogic: IQuanHuyenPageLogic
    ) {
        super();
        this.sanphamPageLogic = sanphamPageLogic;
        this.theloaiPageLogic = theloaiPageLogic;
        this.danhmucPageLogic = danhmucPageLogic;
        this.baomatPageLogic = baomatPageLogic;
        this.trangthaiPageLogic = trangthaiPageLogic;
        this.amthucPageLogic = amthucPageLogic;
        this.tinhthanhPageLogic = tinhthanhPageLogic;
        this.quanhuyenPageLogic = quanhuyenPageLogic;
    }

    @Method.get("/quanlysanpham/")
    @Method.post("/quanlysanpham/")
    public async sanpham(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.sanphamPageLogic.createSanPham({
                    user_cuahang_id: data.user_cuahang_id,
                    danhmuc_id: data.danhmuc_id,
                    theloai_id: data.theloai_id,
                    baomat_id: data.baomat_id,
                    trangthai_id: data.trangthai_id,
                    amthuc_id: data.amthuc_id,
                    tinhthanh_id: data.tinhthanh_id,
                    quanhuyen_id: data.quanhuyen_id,
                    tensanpham: data.tensanpham,
                    hinhanh: data.hinhanh,
                    ngaydang: data.ngaydang,
                    soluong: data.soluong
                });
            }
            form = formResult.form;
        }

        let sanphams = await this.sanphamPageLogic.getSanPhams({
            limit: 5,
            offset: 0
        });

        let danhmucs = await this.danhmucPageLogic.getDanhMucs({
            limit: 5,
            offset: 0
        });

        let theloais = await this.theloaiPageLogic.getTheLoaiSanPhams({
            limit: 5,
            offset: 0
        });

        let baomats = await this.baomatPageLogic.getSanPhamBaoMats({
            limit: 5,
            offset: 0
        });

        let trangthais = await this.trangthaiPageLogic.getSanPhamTrangThais({
            limit: 5,
            offset: 0
        });

        let amthucs = await this.amthucPageLogic.getAmThucs({
            limit: 5,
            offset: 0
        });

        let tinhthanhs = await this.tinhthanhPageLogic.getTinhThanhs({
            limit: 5,
            offset: 0
        });

        let quanhuyens = await this.quanhuyenPageLogic.getQuanHuyens({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "sanpham_sp" : "sanpham", {
            title: "Quản Lý Sản Phẩm",
            form: form,
            sanphams: sanphams ? sanphams.results : null,
            danhmucs: danhmucs ? danhmucs.results : null,
            theloais: theloais ? theloais.results : null,
            baomats: baomats ? baomats.results : null,
            trangthais: trangthais ? trangthais.results : null,
            amthucs: amthucs ? amthucs.results : null,
            tinhthanhs: tinhthanhs ? tinhthanhs.results : null,
            quanhuyens: quanhuyens ? quanhuyens.results : null
        });
    }

    @Method.get("/quanlysanpham/:id/")
    @Method.post("/quanlysanpham/:id/")
    public async sanphamdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamForm;
        let danhmucId: number = parseInt(req.params.id, 10) || 0;
        let sanphamId: number = parseInt(req.params.id, 10) || 0;
        let theloaiId: number = parseInt(req.params.id, 10) || 0;
        let baomatId: number = parseInt(req.params.id, 10) || 0;
        let trangthaiId: number = parseInt(req.params.id, 10) || 0;
        let amthucId: number = parseInt(req.params.id, 10) || 0;
        let tinhthanhId: number = parseInt(req.params.id, 10) || 0;
        let quanhuyenId: number = parseInt(req.params.id, 10) || 0;

        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.sanphamPageLogic.updateSanPham(sanphamId, {
                    user_cuahang_id: data.user_cuahang_id,
                    danhmuc_id: data.danhmuc_id,
                    theloai_id: data.theloai_id,
                    baomat_id: data.baomat_id,
                    trangthai_id: data.trangthai_id,
                    amthuc_id: data.amthuc_id,
                    tinhthanh_id: data.tinhthanh_id,
                    quanhuyen_id: data.quanhuyen_id,
                    tensanpham: data.tensanpham,
                    hinhanh: data.hinhanh,
                    ngaydang: data.ngaydang,
                    soluong: data.soluong
                });
                return res.redirect(`/quanlysanpham/`);
            }
            form = formResult.form;
        }

        let sanpham = await this.sanphamPageLogic.getSanPham(sanphamId);

        let danhmuc = await this.danhmucPageLogic.getDanhMucs(danhmucId);

        let theloai = await this.theloaiPageLogic.getTheLoaiSanPhams(theloaiId);

        let baomat = await this.baomatPageLogic.getSanPhamBaoMats(baomatId);

        let trangthai = await this.trangthaiPageLogic.getSanPhamTrangThais(trangthaiId);

        let amthuc = await this.amthucPageLogic.getAmThucs(amthucId);

        let tinhthanh = await this.tinhthanhPageLogic.getTinhThanhs(tinhthanhId);

        let quanhuyen = await this.quanhuyenPageLogic.getQuanHuyens(quanhuyenId);

        return res.namedView(req.isMobile() ? "sanpham_sp" : "sanphamdetail", {
            title: "Quản Lý Sản Phẩm",
            form: form,
            danhmuc: danhmuc,
            sanpham: sanpham,
            theloai: theloai,
            baomat: baomat,
            trangthai: trangthai,
            amthuc: amthuc,
            tinhthanh: tinhthanh,
            quanhuyen: quanhuyen
        });
    }
}
