/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ITinhThanhPageLogic } from "../pagelogics/tinhthanhPageLogic";
import { tinhthanhForm } from "../forms/tinhthanhForms";

export class TinhThanhController extends Controller {
    static $inject: string[] = ["TinhThanhPageLogic"];

    private tinhthanhPageLogic: ITinhThanhPageLogic;

    constructor(
        tinhthanhPageLogic: ITinhThanhPageLogic
    ) {
        super();
        this.tinhthanhPageLogic = tinhthanhPageLogic;
    }

    @Method.get("/quanlytinhthanh/")
    @Method.post("/quanlytinhthanh/")
    public async tinhthanh(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
      let form = tinhthanhForm;
      if (req.method === "POST") {
          const formResult = await this.handleForm(req, form, true);
          if (formResult.success) {
              const data = formResult.data;
              await this.tinhthanhPageLogic.createTinhThanh({
                  ten: data.ten,
                  trangthai: data.trangthai
              });
          }
          form = formResult.form;
      }

      let tinhthanhs = await this.tinhthanhPageLogic.getTinhThanhs({
          limit: 5,
          offset: 0
      });

        return res.namedView(req.isMobile() ? "tinhthanh_sp" : "tinhthanh", {
            title: "Quản Lý Tỉnh Thành",
            form: form,
            tinhthanhs: tinhthanhs ? tinhthanhs.results : null
        });
    }

    @Method.get("/quanlytinhthanh/:id/")
    @Method.post("/quanlytinhthanh/:id/")
    public async tinhthanhdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = tinhthanhForm;
        let tinhthanhId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.tinhthanhPageLogic.updateTinhThanh(tinhthanhId, {
                    ten: data.ten,
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlytinhthanh/`);
            }
            form = formResult.form;
        }

        let tinhthanh = await this.tinhthanhPageLogic.getTinhThanh(tinhthanhId);

        return res.namedView(req.isMobile() ? "tinhthanh_sp" : "tinhthanhdetail", {
            title: "Quản Lý Tỉnh Thành",
            form: form,
            tinhthanh: tinhthanh
        });
    }
}
