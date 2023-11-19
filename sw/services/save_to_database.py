from sqlalchemy import update
from sqlalchemy.sql.expression import select

import schemas, models
from database import (
    async_session,
    )


async def save_to_database(basho_day):
    async with async_session() as session:
        torikumi_data = basho_day.pop('TorikumiData')

        # TODO FinalMuch is at the moment not used but still persists in json data
        basho_day.pop('FinalMuch')

        basho_day_verified = schemas.BashoDay(**basho_day)

        # check the Basho day is already in DB
        statement = select(models.BashoDay).where(
            models.BashoDay.basho_id == basho_day.get('basho_id'),
            models.BashoDay.kakuzuke_id == basho_day.get('kakuzuke_id'),
            models.BashoDay.day == basho_day.get('day'),
            )
        result = await session.execute(statement)
        basho_day_obj = result.scalars().one()
        if not basho_day_obj:
            basho_day_obj = models.BashoDay(**basho_day_verified.dict())
            session.add(basho_day_obj)
        else:
            session.execute(
                update(models.BashoDay)
                .where(
                    models.BashoDay.basho_id == basho_day.get('basho_id'),
                    models.BashoDay.kakuzuke_id == basho_day.get('kakuzuke_id'),
                    models.BashoDay.day == basho_day.get('day'),
                    )
                .values(**basho_day_verified.dict())
            )

        for bout in torikumi_data:
            east = bout.pop('east')
            west = bout.pop('west')

            bout_verified = schemas.Bout(**bout)

            # validate and create or update east rikishi bout
            east_obj = models.RikishiBout(**east)
            await session.merge(east_obj)

            # validate and create or update west rikishi bout
            west_obj = models.RikishiBout(**west)
            await session.merge(west_obj)

            # check the Bout is already in DB
            statement = select(models.Bout).where(
                models.Bout.east.rikishi_id == east.get('rikishi_id'),
                models.Bout.west.rikishi_id == west.get('rikishi_id'),
                models.Bout.basho_day.id == basho_day_obj.id,
                )
            result = await session.execute(statement)
            bout_obj = result.scalars().one()
            if not bout_obj:
                bout_obj = models.Bout(
                    east=east_obj,
                    west=west_obj,
                    basho_day=basho_day_obj,
                    **bout,
                    )
                session.add(bout_obj)
            else:
                session.execute(
                    update(models.Bout)
                    .where(
                        models.Bout.id == bout_obj.id,
                        )
                    .values(**bout_verified.dict())
                )

        await session.commit()
