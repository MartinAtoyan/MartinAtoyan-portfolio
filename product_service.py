from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductFilter
from app.utils.pagination import apply_filters, apply_pagination


class ProductService:
  @staticmethod
  async def get_all_products(db: AsyncSession, filters: ProductFilter):
      query = await apply_filters(db, filters)
      products = await apply_pagination(query, filters, db)
      return products

  @staticmethod
  async def create_product(db: AsyncSession, product_data: ProductCreate, 
                           current_user):
      print(current_user)
      if current_user.role not in ["admin", "vendor"]:
          raise HTTPException(
              status_code=status.HTTP_403_FORBIDDEN,
              detail="You do not have permission to create a product.")
        
      new_product = Product(**product_data.model_dump(), 
                            vendor_id=current_user.id)
      db.add(new_product)
      await db.commit()
      await db.refresh(new_product)
      return new_product

  @staticmethod
  async def get_product_by_id(db: AsyncSession, product_id: int):
      query = select(Product).where(Product.id == product_id, 
                                    Product.is_deleted == False)
      result = await db.execute(query)
      product = result.scalars().first()
      if not product:
          raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND,
              detail="Product not found."
          )
      return product

  @staticmethod
  async def update_product(db: AsyncSession, product_id: int, 
                           product_data: ProductUpdate, 
                           current_user):
      product = await ProductService.get_product_by_id(db, product_id)
      if not product:
          raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND,
              detail="Product not found.")

      if current_user.role not in ["admin", "vendor"] or (
          current_user.role == "vendor" and product.vendor_id != current_user.id):
          raise HTTPException(
              status_code=status.HTTP_403_FORBIDDEN,
              detail="You do not have permission to update this product.")

      for key, value in product_data.model_dump(exclude_unset=True).items():
          setattr(product, key, value) 

      await db.commit()
      await db.refresh(product)
      return product

  @staticmethod
  async def delete_product(db: AsyncSession, product_id: int, current_user):
      product = await ProductService.get_product_by_id(db, product_id)
      if not product:
          raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND,
              detail="Product not found.")

      if current_user.role not in ("admin", "vendor") \
          or (current_user.role == "vendor" 
              and product.vendor_id != current_user.id):
 
          raise HTTPException(
              status_code=status.HTTP_403_FORBIDDEN,
              detail="You do not have permission to delete this product.")

      product.is_deleted = True
      await db.commit()
      return
