# Product management endpoints
from fastapi import APIRouter, Depends
from app.schemas.product import ProductCreate, ProductFilter, ProductUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.services.product_service import ProductService
from app.utils.token import get_current_user

router =  APIRouter(prefix="/products", tags=['Products'])

@router.get("/")
async def get_all_products(
  filters: ProductFilter = Depends(),
  db: AsyncSession = Depends(get_db)):
  products = await ProductService.get_all_products(db, filters)
  return {"products": products}

@router.post("/")
async def create_product(
  product_data: ProductCreate,
  db: AsyncSession = Depends(get_db),
  current_user = Depends(get_current_user)):
  new_product = await ProductService.create_product(db, product_data, 
                                                      current_user)
  return new_product

@router.get("/{product_id}")
async def get_product(
  product_id: int,
  db: AsyncSession = Depends(get_db)):
  product = await ProductService.get_product_by_id(db, product_id)
  return product

@router.put("/{product_id}")
async def update_product(
  product_id: int,
  product_data: ProductUpdate,
  db: AsyncSession = Depends(get_db),
  current_user = Depends(get_current_user)):
  updated_product = await ProductService.update_product(db, product_id, 
                                                          product_data, 
                                                          current_user)
  return updated_product

@router.delete("/{product_id}")
async def delete_product(
  product_id: int,
  db: AsyncSession = Depends(get_db),
  current_user = Depends(get_current_user)):
  await ProductService.delete_product(db, product_id, current_user)
  return {"detail": "Product deleted successfully."}
