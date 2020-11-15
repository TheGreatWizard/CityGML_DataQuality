
drop sequence if exists citydb.zones_seq cascade;
create sequence citydb.zones_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.zones_seq owner to postgres;

drop table if exists zones;
create table zones (
   id integer not null default nextval('zones_seq'::regclass),
   parent_id integer,
   zone geometry(Polygon,32636) not null,
   module varchar(256),
   existence boolean not null default false,
   completeness numeric(4,3) default null,
   completeness_lod0 numeric(4,3) default null,
   completeness_lod1 numeric(4,3) default null,
   completeness_lod2 numeric(4,3) default null,
   completeness_lod3 numeric(4,3) default null,
   completeness_lod4 numeric(4,3) default null,
   mesh numeric(4,3) default null,
   realistic_texture numeric(4,3) default null,
   texture_resolution numeric default null,
   ce90 numeric default null,
   le90_2d numeric default null,
   se90 numeric default null,
   le90_3d numeric default null,
   measureDate date default null,
   measureTime time default null,
   transience interval default null,
   constraint zones_pk primary key (id),
   constraint zones_parent_fk foreign key (parent_id)
	references citydb.zones (id) match full
	on update cascade
	on delete no action
);


drop sequence if exists citydb.cityobject_dataquality_seq cascade;
create sequence citydb.cityobject_dataquality_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.cityobject_dataquality_seq owner to postgres;

drop type instanceType;
create type instanceType as enum ('all', 'lod0FootPrint','lod0RoofEdge','lod1Solid','lod1MultiSurface','lod1TerrainIntersection','lod2Solid','lod2MultiSurface','lod2MultiCurve','lod2TerrainIntersection','lod3Solid','lod3MultiSurface','lod3MultiCurve','lod3TerrainIntersection','lod4Solid','lod4MultiSurface','lod4MultiCurve','lod4TerrainIntersection');

drop table if exists cityobject_dataquality;
create table cityobject_dataquality (
   id integer not null default nextval('cityobject_dataquality_seq'::regclass),
   instance_type instanceType default 'all',
   cityobject_id integer,
   ce90 numeric default null,
   le90_2d numeric default null,
   se90 numeric default null,
   le90_3d numeric default null,
   completeness numeric(4,3) default null,
   reliability numeric(4,3) default null,
   transience interval default null,
   measureDate date default null,
   measureTime time default null,
   resolution numeric default null,
   texturetype bool default false,

   constraint cityobj_dq_pk primary key (id),
   constraint cityobj_dq_cityobj_fk foreign key (cityobject_id)
   		references citydb.cityobject (id) match full
		on update cascade
        on delete no action
);


drop sequence  if exists citydb.surface_dataquality_seq cascade;
create sequence citydb.surface_dataquality_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.surface_dataquality_seq owner to postgres;

drop table if exists surface_dataquality cascade;
create table surface_dataquality (
   id integer not null default nextval('surface_dataquality_seq'::regclass),
   surface_geometry_id integer,
   position numeric[6] default null,
   azimuth_le90 numeric default null,
   elevation_le90 numeric default null,
   texture_ce90 numeric default null,
   propriety boolean default null,
   occlusion boolean default null,
   distanceToCamera numeric default null,
   verticality numeric default null,
   resolution numeric default null,
   constraint surface_dq_pk primary key (id),
   constraint surface_dq_surface_geom_fk foreign key (surface_geometry_id)
		references citydb.surface_geometry (id) match full
		on update cascade
		on delete no action
);


drop sequence  if exists citydb.surface_position_quality_seq cascade;
create sequence citydb.surface_position_quality_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.surface_position_quality_seq owner to postgres;

drop table if exists surface_position_quality cascade;
create table surface_position_quality (
   id integer not null default nextval('surface_position_quality_seq'::regclass),
   surface_geometry_id integer,
   polygon_index integer,
   position_accuracy numeric[][6] default null,
   constraint surface_pdq_pk primary key (id),
   constraint surface_pdq_surface_geom_fk foreign key (surface_geometry_id)
		references citydb.surface_geometry (id) match full
		on update cascade
		on delete no action
);

drop sequence  if exists citydb.property_dataquality_seq cascade;
create sequence citydb.property_dataquality_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.property_dataquality_seq owner to postgres;

drop table if exists property_dataquality;
create table property_dataquality (
   id integer not null default nextval('property_dataquality_seq'::regclass),
   target_table varchar(255),
   target_property varchar(255),
   target_id integer,
   accuracy numeric default null,
   reliability numeric(4,3) default null,
   measureDate date default null,
   measureTime time default null,
   transience interval default null
);


drop sequence  if exists citydb.building_completeness_seq;
create sequence citydb.building_completeness_seq
    increment 1
    start 1
    minvalue 0
    maxvalue 2147483647
    cache 1;

alter sequence citydb.building_completeness_seq owner to postgres;

drop table if exists building_completeness;
create table building_completeness (
   id integer not null default nextval('building_completeness_seq'::regclass),
   cityobject_id integer,
   completeness	numeric(4,3) default null,
   storey numeric(4,3) default null,
   indoor numeric(4,3) default null,
   texture numeric(4,3) default null,
   constraint bld_complete_cityobj_fk foreign key (cityobject_id)
   		references citydb.cityobject (id) match full
		on update cascade
        on delete no action
);

