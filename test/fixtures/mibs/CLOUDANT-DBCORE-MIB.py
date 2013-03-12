# PySNMP SMI module. Autogenerated from smidump -f python CLOUDANT-DBCORE-MIB
# by libsmi2pysnmp-0.1.3 at Mon Feb 18 15:42:10 2013,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( cloudantTrapLevel, ) = mibBuilder.importSymbols("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel")
( cloudantDbcoreMIB, cloudantModules, ) = mibBuilder.importSymbols("CLOUDANT-REG-MIB", "cloudantDbcoreMIB", "cloudantModules")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

cloudantDbcoreModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 40277, 1, 1, 3)).setRevisions(("2012-07-30 03:00",))
if mibBuilder.loadTexts: cloudantDbcoreModule.setOrganization("Cloudant, Inc.")
if mibBuilder.loadTexts: cloudantDbcoreModule.setContactInfo("580 Harrison Ave., Boston, MA 02118, USA")
if mibBuilder.loadTexts: cloudantDbcoreModule.setDescription("Cloudant DB Core object and event definition MIB")
cloudantDbcoreObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 3, 1, 1))
if mibBuilder.loadTexts: cloudantDbcoreObjects.setDescription("Sub-tree for accessible objects in the MIB.")
cloudantDbcoreShardCount = MibScalar((1, 3, 6, 1, 4, 1, 40277, 3, 1, 1, 1), Integer32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: cloudantDbcoreShardCount.setDescription("The number of shards associated with an event")
cloudantDbcoreEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2))
if mibBuilder.loadTexts: cloudantDbcoreEvents.setDescription("A sub-tree for all the CLOUDANT-DBCORE-MIB related events\nand traps.")

# Augmentions

# Notifications

cloudantDbcoreRebootEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2, 1)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ) )
if mibBuilder.loadTexts: cloudantDbcoreRebootEvent.setDescription("This event is generated when the DB Core service is restarted\non the given node.")
cloudantDbcoreShardsUnavailableEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2, 2)).setObjects(*(("CLOUDANT-DBCORE-MIB", "cloudantDbcoreShardCount"), ("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ) )
if mibBuilder.loadTexts: cloudantDbcoreShardsUnavailableEvent.setDescription("This event is generated when the DB Core service detects\nunavailable shards in the cluster.")
cloudantDbcoreShardsImpairedEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2, 3)).setObjects(*(("CLOUDANT-DBCORE-MIB", "cloudantDbcoreShardCount"), ("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ) )
if mibBuilder.loadTexts: cloudantDbcoreShardsImpairedEvent.setDescription("This event is generated when the DB Core service detects\nimpaired shards in the cluster.")
cloudantDbcoreAllShardsAvailableEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2, 4)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ) )
if mibBuilder.loadTexts: cloudantDbcoreAllShardsAvailableEvent.setDescription("This event is generated when the DB Core service detects\nthat all data in the cluster is available again.")
cloudantDbcoreAllShardsUnimpairedEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 1, 2, 5)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ) )
if mibBuilder.loadTexts: cloudantDbcoreAllShardsUnimpairedEvent.setDescription("This event is generated when the DB Core service detects\nthat all data in the cluster is fully protected again.")

# Exports

# Module identity
mibBuilder.exportSymbols("CLOUDANT-DBCORE-MIB", PYSNMP_MODULE_ID=cloudantDbcoreModule)

# Objects
mibBuilder.exportSymbols("CLOUDANT-DBCORE-MIB", cloudantDbcoreModule=cloudantDbcoreModule, cloudantDbcoreObjects=cloudantDbcoreObjects, cloudantDbcoreShardCount=cloudantDbcoreShardCount, cloudantDbcoreEvents=cloudantDbcoreEvents)

# Notifications
mibBuilder.exportSymbols("CLOUDANT-DBCORE-MIB", cloudantDbcoreRebootEvent=cloudantDbcoreRebootEvent, cloudantDbcoreShardsUnavailableEvent=cloudantDbcoreShardsUnavailableEvent, cloudantDbcoreShardsImpairedEvent=cloudantDbcoreShardsImpairedEvent, cloudantDbcoreAllShardsAvailableEvent=cloudantDbcoreAllShardsAvailableEvent, cloudantDbcoreAllShardsUnimpairedEvent=cloudantDbcoreAllShardsUnimpairedEvent)
