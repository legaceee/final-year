import {Router} from "express";
import { signup } from "../controller/authController";

const router=Router();
router.post("/signup",signup);
router.post("/signin");
export default router;