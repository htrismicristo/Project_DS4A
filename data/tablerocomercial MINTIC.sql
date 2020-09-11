USE [BI]
GO

/****** Object:  Table [dbo].[TableroComercial]    Script Date: 14/08/2020 8:34:54 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[TableroComercial](
	[NoFactura] [varchar](10) NULL,
	[ClaseFactura] [varchar](4) NULL,
	[DesClaseFactura] [varchar](20) NULL,
	[FacturaAnulada] [varchar](1) NULL,
	[FechaFactura] [varchar](35) NULL,
	[HoraFactura] [varchar](20) NULL,
	[Material] [varchar](18) NULL,
	[DesMaterial] [varchar](40) NULL,
	[GrupoArticulo] [varchar](10) NULL,
	[DesGrArticulo] [varchar](30) NULL,
	[TipoMaterial] [varchar](4) NULL,
	[DesTipoMaterial] [varchar](30) NULL,
	[GrupoMateriales] [varchar](5) NULL,
	[DescGrupoMateriales] [varchar](30) NULL,
	[Categoria] [varchar](5) NULL,
	[DesCategoria] [varchar](30) NULL,
	[ClaseMaterial] [varchar](5) NULL,
	[DesClaseMaterial] [varchar](30) NULL,
	[Topologia] [varchar](5) NULL,
	[DesTopologia] [varchar](30) NULL,
	[Color] [varchar](5) NULL,
	[DesColor] [varchar](30) NULL,
	[CompradoProducido] [varchar](5) NULL,
	[DesCompradoProducido] [varchar](30) NULL,
	[CantFacturada] [decimal](18, 3) NULL,
	[UMB] [varchar](5) NULL,
	[ValorNeto] [decimal](18, 3) NULL,
	[ValorToral] [decimal](18, 3) NULL,
	[ValCostoTotalPos] [decimal](18, 3) NULL,
	[ValCostoUnitario] [decimal](18, 3) NULL,
	[Descuento] [decimal](18, 3) NULL,
	[IVA] [decimal](18, 3) NULL,
	[FletePosicion] [decimal](18, 3) NULL,
	[PosComboPadre] [varchar](6) NULL,
	[Centro] [varchar](5) NULL,
	[Almacen] [varchar](5) NULL,
	[OrgVta] [varchar](4) NULL,
	[Canal] [varchar](2) NULL,
	[ZonaVenta] [varchar](6) NULL,
	[DesZonaVtas] [varchar](20) NULL,
	[Solicitante] [varchar](10) NULL,
	[NombreSolicitante] [varchar](40) NULL,
	[Pagador] [varchar](10) NULL,
	[NombrePagador] [varchar](40) NULL,
	[Pais] [varchar](30) NULL,
	[Ciudad] [varchar](35) NULL,
	[EdadProducto] [varchar](30) NULL,
	[Recompra] [bit] NULL,
	[DiasNoCompra] [int] NULL
	[MaterialNuevo] [varchar](4) NULL,
	[CondicionPago] [varchar](6) NULL,
	[DesCondicionPago] [varchar](40) NULL,
	[OficVentas] [varchar](4) NULL,
	[GrVendedor] [varchar](3) NULL,
	[DescGrpoVendedor] [varchar](40) NULL,
	[NombreVendedorPDP] [varchar](50) NULL,
	[CEBE] [varchar](10) NULL,
	[AnoMes] [varchar](7) NULL,
	[CodGerencia] [varchar](5) NULL,
	[DesGerencia] [varchar](30) NULL,
	[LPrecio] [varchar](3) NULL,
	[NoPedidoCliente] [varchar](20) NULL,
	[Ped_NoPedOrig] [varchar](30) NULL,
	[Ped_Fecha] [varchar](30) NULL,
	[Ped_NoPosOrig] [varchar](30) NULL,
	[HoraPedido] [varchar](20) NULL,
	[Entrega] [varchar](20) NULL,
	[FechaEntrega] [varchar](30) NULL,
	[HoraEntrega] [varchar](20) NULL,
	[DocModelo] [varchar](10) NULL,
	[Fechaproceso] [datetime] NULL,	
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


