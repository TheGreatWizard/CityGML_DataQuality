drop sequence if exists citydb.zones_seq cascade;
drop sequence if exists citydb.cityobject_dataquality_seq cascade;
drop sequence if exists citydb.surface_dataquality_seq cascade;
drop sequence if exists  citydb.property_dataquality_seq cascade;
drop sequence if exists citydb.building_completness_seq cascade;

drop table if exists zones;
alter table if exists cityobject_dataquality drop constraint cityobj_dq_cityobj_fk;
drop table if exists cityobject_dataquality;
alter table if exists surface_dataquality drop constraint surface_dq_surface_geom_fk;
drop table if exists surface_dataquality;
drop table if exists property_dataquality;
alter table if exists building_completness drop constraint bld_complete_cityobj_fk;
drop table if exists building_completness;